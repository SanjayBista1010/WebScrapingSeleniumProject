import os
import sys
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.logger import logger
from src.exception import CustomException
from src.utils import save_to_csv, is_duplicate

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "headlines.csv")


def fetch_and_save_headline():
    try:
        # Setup headless Chrome
        options = Options()
        options.headless = True
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        url = "https://english.onlinekhabar.com/"
        driver.get(url)

        # Get first headline
        article = driver.find_element(By.CSS_SELECTOR, "div.ok-post-contents")
        headline_tag = article.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
        author_tag = article.find_element(By.CSS_SELECTOR, "span.ok-post-hours")

        headline = headline_tag.text.strip()
        link = headline_tag.get_attribute("href")
        author = author_tag.text.strip() if author_tag else "Unknown"

        driver.quit()

        # Prevent duplicate headline
        if is_duplicate(DATA_PATH, headline, column_index=1):
            logger.info("No new headline. Skipping: %s", headline)
            return

        # Save new headline
        save_to_csv(
            DATA_PATH,
            [datetime.now(), headline, author, link],
            headers=["Fetched At", "Headline", "Author", "Link"]
        )
        logger.info("Saved headline: %s", headline)

    except Exception as e:
        logger.error("Exception occurred in scraper")
        raise CustomException(e, sys)
