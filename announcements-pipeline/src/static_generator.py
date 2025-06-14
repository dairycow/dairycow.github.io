"""
Static Site Generator for ASX Dashboard
"""

import json
from pathlib import Path
from datetime import datetime
from jinja2 import Template
import markdown


def generate_static_site(output_dir: str = './output') -> None:
    """Generate static site from latest summaries"""
    summaries, date_str = get_latest_summaries(output_dir)
    
    # Load template
    module_dir = Path(__file__).parent.parent
    template_path = module_dir / 'templates' / 'index.html'
    template = Template(template_path.read_text(encoding='utf-8'))
    
    # Generate HTML
    html = template.render(
        summaries=summaries,
        date=format_date(date_str),
        total_count=len(summaries),
        format_time=format_time
    )
    
    # Write files
    site_path = module_dir / 'site' / 'asx'
    site_path.mkdir(parents=True, exist_ok=True)

    (site_path / 'index.html').write_text(html, encoding='utf-8')
    (site_path / 'api.json').write_text(
        json.dumps(summaries, indent=2), 
        encoding='utf-8'
    )
    
    print(f"Generated site with {len(summaries)} summaries")


def get_latest_summaries(output_dir: str) -> tuple:
    """Get summaries from most recent date folder"""
    output_path = Path(output_dir)
    
    # Find latest date folder
    date_folders = [d for d in output_path.iterdir() if d.is_dir()]

    if not date_folders:
        return [], None
    
    latest_folder = max(date_folders, key=lambda x: x.name)
    
    # Load summaries
    markdowner = markdown.Markdown()
    summaries = []
    for summary_file in latest_folder.glob('*.json'):
        try:
            summary = json.loads(summary_file.read_text(encoding='utf-8'))
            # Only include summaries that actually have content
            if summary.get('summary') and summary.get('summary').strip():
                # convert markdown to HTML if needed
                summary['summary'] = markdowner.convert(summary['summary'])
                summaries.append(summary)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Warning: Could not parse {summary_file}: {e}")
            continue
    
    # Sort by time (latest first)
    summaries.sort(key=lambda x: x.get('time', ''), reverse=True)
    
    return summaries, latest_folder.name


def format_date(date_str: str) -> str:
    """Convert YYYYMMDD to readable format"""
    try:
        date_obj = datetime.strptime(date_str, '%Y%m%d')
        return date_obj.strftime('%-d %B %Y')
    except ValueError:
        return date_str


def format_time(time_str: str) -> str:
    """Format time string as HH:MM"""
    if not time_str or len(time_str) != 4:
        return time_str or 'N/A'
    return f"{time_str[:2]}:{time_str[2:]}"
