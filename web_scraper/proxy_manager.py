# web_scraper/proxy_manager.py
import random
import logging

# Empty list for now (proxies disabled safely)
PROXIES = []

def get_random_proxy():
    """
    Returns a proxy dict for requests
    Returns None if no proxies are configured
    """
    if not PROXIES:
        logging.info("No proxies configured, using direct connection")
        return None

    proxy = random.choice(PROXIES)
    return {
        "http": proxy,
        "https": proxy
    }
