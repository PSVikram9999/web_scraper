
# Web Scraping & Automation: E-Commerce Price Tracker

## Overview
Python script to scrape product prices from Flipkart using Selenium and BeautifulSoup. Prices are stored in a SQLite DB and optional alerts are triggered.

## Features
- Scrape multiple products
- Save to SQLite database
- Email alert on price drop (optional)
- Can be automated using `schedule` or `cron`

## Run Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run script:
   ```
   python scraper.py
   ```

## Notes
- Flipkart content loads via JS, so Selenium is required.
- Make sure to set up ChromeDriver in your PATH.
