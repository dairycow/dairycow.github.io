"""ASX Announcement Summarizer"""

import json
import requests
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional


def check_openrouter_api_limits(api_key: str) -> dict:
    """Check current API key limits and usage"""
    response = requests.get(
        url="https://openrouter.ai/api/v1/auth/key",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    response.raise_for_status()
    
    data = response.json()['data']
    
    limits_info = {
        'daily_limit': data.get('limit'),
        'daily_usage': data.get('usage'),
        'daily_remaining': data.get('limit_remaining'),
        'rate_limit_requests': data.get('rate_limit').get('requests'),
        'rate_limit_interval': data.get('rate_limit').get('interval'),
        'is_free_tier': data.get('is_free_tier')
    }
    
    return limits_info


def generate_response(text: str, api_url: str, api_key: str, model: str = 'deepseek/deepseek-chat-v3-0324:free') -> Optional[dict]:
    """Generate API response for text summarization"""
    prompt = load_prompt()
    
    payload = {
        "model": model,
        "messages": [{
            "role": "user", 
            "content": f"{prompt}\n\n{text}"
        }]
    }
    
    response = requests.post(
        api_url,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=payload,
        timeout=60
    )
    
    response.raise_for_status()
    return response.json()


def load_prompt() -> str:
    """Load summarization prompt"""
    prompt_file = Path(__file__).parent.parent / 'config' / 'summarization_prompt.txt'
    return prompt_file.read_text(encoding='utf-8').strip()


def find_unprocessed_files(output_dir: str = './output') -> List[Path]:
    """Find .txt files without summaries in their .json metadata"""
    files = []
    output_path = Path(output_dir)
    
    for txt_file in output_path.rglob('*.txt'):
        json_file = txt_file.with_suffix('.json')
        
        if json_file.exists():
            try:
                metadata = json.loads(json_file.read_text())
                # Check if summary already exists
                if not metadata.get('summary'):
                    files.append(txt_file)
            except:
                # If JSON is corrupted, consider it unprocessed
                files.append(txt_file)
        else:
            # No JSON file means unprocessed
            files.append(txt_file)
    
    return files


def process_all_files(api_url: str, api_key: str, output_dir: str = './output') -> Dict:
    """Process all unprocessed files and update their JSON metadata"""
    files = find_unprocessed_files(output_dir)
    
    if not files:
        print("✅ All files already have summaries")
        return {'processed': 0, 'total': 0, 'skipped': 0}
    
    print(f"📝 Found {len(files)} files to summarize")
    
    processed = 0
    for txt_file in files:
        if process_single_file(txt_file, api_url, api_key):
            processed += 1
    
    return {
        'processed': processed,
        'total': len(files),
        'skipped': len(files) - processed
    }


def process_single_file(txt_file: Path, api_url: str, api_key: str) -> bool:
    """Process a single text file and update its JSON metadata"""
    try:
        # Read the text content
        text = txt_file.read_text(encoding='utf-8')
        
        # Generate summary
        response = generate_response(text, api_url, api_key)
        
        # Update the corresponding JSON file
        json_file = txt_file.with_suffix('.json')
        metadata = json.loads(json_file.read_text())
        
        # Add summary data
        metadata.update({
            'summary': response['choices'][0]['message']['content'],
            'usage': response['usage'],
            'model': response['model'],
            'processed_at': datetime.now().isoformat()
        })
        
        # Save updated metadata
        json_file.write_text(json.dumps(metadata, indent=2), encoding='utf-8')
        
        print(f"✅ Summarized: {txt_file.name}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {txt_file.name}: {e}")
        return False
