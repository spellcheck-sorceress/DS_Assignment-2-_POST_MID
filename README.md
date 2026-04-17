# DS_Assignment-2-_POST_MID
DS Assignment 2 (post mid): Web Scraping &amp;GitHub Data Management 

# SUBMITTED BY MARYAM SANA (F23BSCS017)

# Books Toscrape Web Scraper

### 1. Project Overview
* **Target Website:** http://books.toscrape.com
* **Data Fields Extracted:** Title, Price, Rating
* **Tools Used:** Python, requests, BeautifulSoup4, pandas

### 2. Setup Instructions
1. Clone this repo: `git clone https://github.com/spellcheck-sorceress/DS_Assignment-2-_POST_MID`
2. Install dependencies: `pip install -r requirements.txt`
3. Run script: `python scraper.py`

### 3. Challenges & Solutions
* The scraper needed to handle pagination across 50 pages. This was solved by detecting the "next" button in the HTML after each page and dynamically constructing the next page URL until no next button was found.
