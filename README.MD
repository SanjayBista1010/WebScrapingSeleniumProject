# Web Scraping Selenium Project

This project scrapes the latest news headlines from [OnlineKhabar English](https://english.onlinekhabar.com/) and stores them in a CSV file.

## Features
- Scrapes the **first headline** from OnlineKhabar English.
- Prevents duplicate entries.
- Saves data in `data/headlines.csv`.
- Runs automatically using **GitHub Actions**.
- Commits and pushes updates directly to the repository.

## File Structure
```
.
├── data/
│   └── headlines.csv       # Stored headlines
├── src/
│   ├── logger.py           # Logging utility
│   ├── exception.py        # Custom exception handler
│   ├── utils.py            # Helper functions (CSV, duplicate check)
│   └── scraper.py          # Main scraper logic
├── main.py                 # Entry point
├── .github/
│   └── workflows/
│       └── scraper.yml     # GitHub Actions workflow
└── README.md               # Project documentation
```

## How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/SanjayBista1010/WebScrapingSeleniumProject.git
   cd WebScrapingSeleniumProject
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the scraper:
   ```bash
   python main.py
   ```

## GitHub Actions
- The scraper runs on a schedule (every 2 hours).
- If a new headline is found, it is committed and pushed automatically.

## Author
**Sanjay Bista**  
