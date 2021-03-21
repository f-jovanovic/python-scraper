import requests

from urllib.parse import urlparse
from bs4 import BeautifulSoup

from classes.pagedata import PageData
from scraper.logoscraper import get_logo
from scraper.phonescraper import get_phones


def scrape_page(page_url):
    page_url = page_url.strip()
    try:
        response = requests.get(page_url)

    except requests.RequestException:
        return f"The URL is invalid | URL: {page_url}"

    if response and response.ok and response.text:
        page_body = BeautifulSoup(response.text, "html.parser").find("body")
        response_parsed = urlparse(response.url)
        page_logo = get_logo(
            page_body,
            f"{response_parsed.scheme}://{response_parsed.netloc}",
        )
        phone_list = get_phones(page_body)
        return PageData(page_url, page_logo, phone_list).to_json()

    else:
        return f"The provided URL is unreachable | URL: {page_url} | Status code: {response.status_code}"
