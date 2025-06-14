# ASX Announcements

Automated pipeline that scrapes, processes and summarizes ASX company announcements.

## Features

- **Scrapes** latest ASX announcements 
- **Extracts** text from PDF documents
- **Summarizes** using AI (OpenRouter API)
- **Generates** static site with announcements
- **Deploys** automatically via GitHub Actions

## Pipeline

Runs every 3 minutes during Sydney trading hours (7:30 AM - 7:30 PM, Mon-Fri) and:

1. Fetches recent announcements from ASX
2. Downloads and extracts text from PDFs
3. Generates AI summaries of announcements
4. Builds static HTML site
5. Deploys to `/asx` folder

## Setup

1. Set `OPENROUTER_API_KEY` in GitHub repository secrets
2. Pipeline runs automatically via GitHub Actions

## Local Development

```bash
cd announcements-pipeline
pip install -r requirements.txt
python run_pipeline.py
```

Requires `.env` file with `OPENROUTER_API_KEY` for local