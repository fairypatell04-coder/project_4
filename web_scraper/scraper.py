# web_scraper/scraper.py

import requests
from bs4 import BeautifulSoup
import logging
import csv
import os

from .user_agents import get_random_user_agent
from .proxy_manager import get_random_proxy


class WebScraper:
    """Web scraper with User-Agent rotation and optional proxy support"""

    def __init__(self, url, output_file="exports/scraper_output.csv"):
        self.url = url
        self.output_file = output_file
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

    def scrape(self):
        headers = {
            "User-Agent": get_random_user_agent()
        }

        proxy = get_random_proxy()

        if proxy:
            logging.info(f"Scraping {self.url} using proxy")
        else:
            logging.info(f"Scraping {self.url} without proxy")

        try:
            response = requests.get(
                self.url,
                headers=headers,
                proxies=proxy,   # None or dict — both valid
                timeout=10
            )
            response.raise_for_status()

        except Exception as e:
            logging.error(f"Failed to fetch {self.url}: {e}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        data = []
        for a in soup.find_all("a", href=True):
            data.append({
                "text": a.text.strip(),
                "href": a["href"]
            })

        self._export_csv(data)
        logging.info(f"Scraping completed: {len(data)} links found")

        return data

    def _export_csv(self, data):
        with open(self.output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["text", "href"])
            writer.writeheader()
            writer.writerows(data)

        logging.info(f"Exported data to {self.output_file}")
