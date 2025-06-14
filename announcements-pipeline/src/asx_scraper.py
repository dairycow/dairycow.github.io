"""ASX Announcement PDF URL Scraping Module"""

import requests
from typing import Dict, List, Optional
from bs4 import BeautifulSoup

# TODO: Update to use the latest ASX announcements URL
# ASX_ANNOUNCEMENTS_URL = "https://www.asx.com.au/asx/v2/statistics/todayAnns.do"
ASX_ANNOUNCEMENTS_URL = "https://www.asx.com.au/asx/v2/statistics/prevBusDayAnns.do"
ASX_BASE_URL = "https://www.asx.com.au"
DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0'}


def fetch_announcements() -> List[Dict]:
    """Fetch and parse all current ASX announcements."""
    response = requests.get(ASX_ANNOUNCEMENTS_URL, headers=DEFAULT_HEADERS, timeout=30)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    rows = soup.select('table tr')[1:]
    announcements = []
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 4:
            if announcement := parse_row(cells):
                announcements.append(announcement)
    
    return announcements


def parse_row(cells) -> Optional[Dict]:
    """Extract announcement details from table row."""
    ticker = cells[0].get_text(strip=True)
    pdf_href = cells[3].find('a').get('href')

    if not ticker or not pdf_href:
        return None
    
    return {
        'ticker': ticker,
        'pdf_display_url': ASX_BASE_URL + pdf_href,
        'id': pdf_href.split('idsId=')[1] if 'idsId=' in pdf_href else '',
        'pages': extract_page_count(cells[3]),
        'price_sensitive': bool(cells[2].find('img', class_='pricesens')),
        'date': normalize_date(cells[1].get_text().split('\n')[1].strip()),
        'time': normalize_time(cells[1].get_text().split('\n')[2].strip()),
    }


def extract_page_count(cell) -> int:
    """Extract page count from PDF link cell."""
    page_span = cell.find('span', class_='page')
    page_text = page_span.get_text().strip()
    page_number = page_text.split()[0]
    return int(page_number)


def normalize_time(time_str: str) -> str:
    """Convert to 24-hour format."""
    try:
        if 'pm' in time_str:
            hour, minute = time_str.replace(' pm', '').split(':')
            hour = int(hour)
            if hour != 12:
                hour += 12
        else:
            hour, minute = time_str.replace(' am', '').split(':')
            hour = int(hour)
            if hour == 12:
                hour = 0
        return f"{hour:02d}{minute}"
    except:
        return "0000"


def normalize_date(date_str: str) -> str:
    """Convert date from DD/MM/YYYY format to YYYYMMDD."""
    if not date_str or '/' not in date_str:
        return ""
    
    try:
        day, month, year = date_str.strip().split('/')
        return f"{year}{month.zfill(2)}{day.zfill(2)}"
    except ValueError:
        return ""


def get_direct_pdf_url(pdf_display_url: str) -> str:
    """Get direct PDF URL from display page."""
    response = requests.get(pdf_display_url, headers=DEFAULT_HEADERS, timeout=30)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_input = soup.find('input', {'name': 'pdfURL'})
    
    if not pdf_input or not pdf_input.get('value'):
        raise ValueError(f"PDF URL not found in {pdf_display_url}")
    
    return pdf_input['value']
