import os
import sys
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from src.logger import logger
from src.exception import CustomException
from src.utils import save_to_csv, is_duplicate

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "headlines.csv")


def fetch_and_save_headline():
    try:
        # Setup headless Firefox
        options = Options()
        options.headless = True

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

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
