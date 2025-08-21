import sys
import time
import random
from src.scrapper import fetch_and_save_headline
from src.logger import logger
from src.exception import CustomException


def main():
    try:
        # Random delay between 0 and 5 minutes (0–300 seconds)
        sleep_time = random.randint(0, 300)
        logger.info(f"⏱ Sleeping for {sleep_time} seconds before running scraper")
        time.sleep(sleep_time)

        logger.info("🚀 Scraper started")
        fetch_and_save_headline()
        logger.info("✅ Scraper finished successfully")

    except Exception as e:
        logger.error("❌ An error occurred while running the scraper")
        raise CustomException(e, sys)


if __name__ == "__main__":
    main()
