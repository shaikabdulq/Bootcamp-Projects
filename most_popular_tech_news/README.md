# Hacker News Scraper

## Overview
This project consists of a Python script designed to scrape the Hacker News website for the most upvoted article. It uses the `requests` and `BeautifulSoup` libraries to parse the website and extract relevant information.

## Features
- Scrapes the [Hacker News](https://news.ycombinator.com/) website.
- Extracts articles along with their upvote scores.
- Identifies the most upvoted article and displays its link and title.

## Requirements
- Python 3.9 or lower (due to compatibility issues with the `BeautifulSoup` module).
- `requests` library.
- `BeautifulSoup` library.

## Usage
Run the `main.py` script to fetch the most upvoted article from Hacker News. The output will display the link and title of the article.

## Note
The project is currently set up to work with the specific structure of the Hacker News website as of its last update. Any significant changes to the site's HTML structure may require modifications to the script.

## Additional Files
- `website.html`: An example HTML file, not directly related to the functionality of the scraper, but included for reference.
