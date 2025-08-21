import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import sys

from src.logger import logger
from src.exception import CustomException
from src.utils import save_to_csv, is_duplicate

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "headlines.csv")

def fetch_and_save_headline():
    try:
        url = "https://english.onlinekhabar.com/"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        article = soup.find("div", class_="ok-post-contents")
        if not article:
            logger.warning("No headline found.")
            return

        headline_tag = article.find("h2").find("a")
        author_tag = article.find("span", class_="ok-post-hours")

        headline = headline_tag.text.strip()
        link = headline_tag["href"]
        author = author_tag.text.strip() if author_tag else "Unknown"

        # Prevent duplicate headline
        if is_duplicate(DATA_PATH, headline, column_index=1):  
            logger.info("No new headline. Skipping: %s", headline)
            return

        # Save new headline
        save_to_csv(
            DATA_PATH,
            [datetime.now(), headline, author, link],
            headers=["Fetched At", "Headline", "Author", "Link"],
        )
        logger.info("Saved headline: %s", headline)

    except Exception as e:
        logger.error("Exception occurred in scraper")
        raise CustomException(e, sys)
