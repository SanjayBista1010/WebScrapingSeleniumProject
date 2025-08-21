import os
import sys
from datetime import datetime
import requests
import csv
from bs4 import BeautifulSoup

from src.logger import logger
from src.exception import CustomException
from src.utils import save_to_csv, is_duplicate

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "headlines.csv")


def fetch_and_save_headline():
    try:
        url = "https://english.onlinekhabar.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        # Get the first article
        article = soup.find("div", class_="ok-post-contents")
        if not article:
            logger.warning("No headline found.")
            return

        headline_tag = article.find("h2").find("a")
        author_tag = article.find("span", class_="ok-post-hours")

        headline = headline_tag.text.strip()
        link = headline_tag["href"]
        author = author_tag.text.strip() if author_tag else "Unknown"

        # Skip duplicate headline
        if os.path.isfile(DATA_PATH):
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                exists = any(row[1] == headline for row in csv.reader(f))
            if exists:
                logger.info("No new headline. Skipping: %s", headline)
                return

        # Save new headline
        file_exists = os.path.isfile(DATA_PATH)
        with open(DATA_PATH, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Fetched At", "Headline", "Author", "Link"])
            writer.writerow([datetime.now(), headline, author, link])

        logger.info("Saved headline: %s", headline)

    except Exception as e:
        logger.error("Exception occurred in scraper")
        raise CustomException(e, sys)
