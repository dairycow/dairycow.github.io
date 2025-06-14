"""Complete ASX Announcements Pipeline"""

import os
from datetime import datetime, time
from pathlib import Path
import shutil

import holidays
import pytz
from dotenv import load_dotenv

from src.asx_scraper import fetch_announcements
from src.pdf_extractor import process_announcement
from src.summarizer import process_all_files
from src.static_generator import generate_static_site


load_dotenv()

MAX_ANNOUNCEMENTS = 30 # Maximum announcements to save per run
MAX_PAGE_COUNT = 50  # Maximum pages to process per announcement


def is_trading_day() -> bool:
    """Check if today is a trading day (not weekend or Australian public holiday)"""
    sydney_tz = pytz.timezone('Australia/Sydney')
    today = datetime.now(sydney_tz).date()
    if today.weekday() > 4:
        return False
    au_holidays = holidays.Australia(state='NSW', years=today.year)
    return today not in au_holidays


def is_announcement_time() -> bool:
    """Check if current time is within ASX announcement window (10:00 to 16:00 Sydney time)"""
    sydney_tz = pytz.timezone('Australia/Sydney')
    sydney_time = datetime.now(sydney_tz)
    start_time = time(7, 30)
    end_time = time(19, 30)

    current_time = sydney_time.time()
    return start_time <= current_time < end_time


def run_complete_pipeline():
    """Run end-to-end ASX announcements pipeline"""
    
    if not is_trading_day():
        return
        
    if not is_announcement_time():
        return
    
    announcements = fetch_announcements()
    if not announcements:
        return
    
    # Extract text
    for announcement in announcements[0:MAX_ANNOUNCEMENTS]:
        if announcement['pages'] > MAX_PAGE_COUNT:
            continue
        process_announcement(announcement)

    # Generate summaries
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    api_key = os.getenv('OPENROUTER_API_KEY')
    process_all_files(api_url, api_key)

    generate_static_site()

    deploy_to_asx_folder()


def deploy_to_asx_folder():
    """Deploy generated site to asx folder"""
    module_dir = Path(__file__).parent
    asx_path = module_dir / ".." / "asx"
    # Remove existing contents
    for item in asx_path.iterdir():
        item.unlink()
    # Copy contents from site/asx to asx
    site_path = module_dir / "site" / "asx"
    for item in site_path.iterdir():
        dst = asx_path / item.name
        shutil.copy2(item, dst)


if __name__ == "__main__":
    run_complete_pipeline()