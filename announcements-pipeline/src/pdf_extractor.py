"""Minimalist PDF text extraction for ASX announcements."""

import fitz
import requests
import json
from pathlib import Path
from typing import Dict


def extract_text_from_pdf_url(pdf_url: str) -> str:
    """Download and extract text from PDF URL."""
    response = requests.get(pdf_url)
    response.raise_for_status()
    
    with fitz.open(stream=response.content, filetype="pdf") as doc:
        return "\n".join(page.get_text() for page in doc).strip()


def get_output_path(announcement: Dict, output_dir: str = './output') -> Path:
    return Path(output_dir) / announcement['date'] / announcement['id']


def is_already_extracted(announcement: Dict, output_dir: str = './output') -> bool:
    """Check if both text and metadata files already exist."""
    base_path = get_output_path(announcement, output_dir)
    txt_exists = base_path.with_suffix('.txt').exists()
    json_exists = base_path.with_suffix('.json').exists()
    return txt_exists and json_exists


def save_announcement_data(announcement: Dict, pdf_url: str, text: str, output_dir: str = './output') -> bool:
    """Save extracted text and metadata to organized directory structure."""
    try:
        base_path = get_output_path(announcement, output_dir)
        base_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save extracted text
        base_path.with_suffix('.txt').write_text(text, encoding='utf-8')
        
        # Save metadata
        metadata = {
            **announcement,
            'pdf_url': pdf_url,
        }
        base_path.with_suffix('.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
        
        return True
    except Exception:
        return False


def process_announcement(announcement: Dict, output_dir: str = './output') -> bool:
    """Extract and save announcement if not already processed."""
    if is_already_extracted(announcement, output_dir):
        return True
    
    try:
        from .asx_scraper import get_direct_pdf_url
        
        pdf_url = get_direct_pdf_url(announcement['pdf_display_url'])
        text = extract_text_from_pdf_url(pdf_url)
        
        return save_announcement_data(announcement, pdf_url, text, output_dir)
    except Exception:
        return False
