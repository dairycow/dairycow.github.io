# dairycow.github.io

Personal GitHub Pages site with automated content pipelines.

## Structure

```
├── asx/                          # ASX announcements site (auto-generated)
├── announcements-pipeline/       # ASX scraping and processing pipeline
├── .github/workflows/            # GitHub Actions 
```

## Projects

### ASX Announcements Pipeline
Automated scraper that processes ASX company announcements, extracts text from PDFs, generates AI summaries, and publishes to a static site.

- **Live site**: [https://gibx.au/asx](https://gibx.au/asx)
- **Pipeline code**: [/announcements-pipeline](./announcements-pipeline)

## License

MIT License - see [LICENSE](LICENSE) file for details.