# 📰 OnlineKhabar Headline Scraper

This project scrapes the latest news headline from [OnlineKhabar English](https://english.onlinekhabar.com/) and saves it into a CSV file (`data/headlines.csv`).  
It also runs automatically every hour using **GitHub Actions** and commits new headlines to this repository.

---

## 📂 Project Structure

```
├── data/
│   └── headlines.csv      # Collected headlines
├── src/
│   ├── scrapper.py        # Scraper logic
│   ├── utils.py           # Helper functions (CSV save, duplicate check)
│   ├── logger.py          # Logging setup
│   └── exception.py       # Custom exception handler
├── main.py                # Entry point to run scraper
├── requirements.txt       # Dependencies
└── .github/workflows/
    └── scraper.yml        # GitHub Actions workflow
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/SanjayBista1010/WebScrapingSeleniumProject.git
cd WebScrapingSeleniumProject
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the scraper manually
```bash
python main.py
```

This will:
- Fetch the latest headline
- Append it to `data/headlines.csv` (if not already present)
- Log the result in console and log files

---

## 🤖 Automation with GitHub Actions

The scraper runs **every hour** on GitHub Actions and commits new headlines back to this repo.

- Workflow file: `.github/workflows/scraper.yml`
- Commit format:  
  ```
  Update headlines [skip ci]
  ```

You can also run it manually from the **Actions** tab.

---

## 📝 Example CSV Output

```csv
Fetched At,Headline,Author,Link
2025-08-21 12:00:00,Example Headline,2 hours ago,https://english.onlinekhabar.com/example-news
```

---

## 👨‍💻 Author
**Sanjay Bista**  


