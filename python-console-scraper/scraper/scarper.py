import requests
import urllib.parse as urlparser

from bs4 import BeautifulSoup

from classes.pagedata import PageData
from scraper.logoscraper import get_logo
from scraper.phonescraper import get_phones


def scrape_page(pageurl):
    pageurl = pageurl.strip()
    try:
        response = requests.get(pageurl)

    except requests.RequestException:
        return f"The URL is invalid | URL: {pageurl}"

    if response and response.ok and response.text:
        pagebody = BeautifulSoup(response.text, "html.parser").find("body")
        pagelogo = get_logo(
            pagebody,
            f"{urlparser.urlparse(response.url).scheme}://{urlparser.urlparse(response.url).netloc}",
        )
        phonelist = get_phones(pagebody)
        return PageData(pageurl, pagelogo, phonelist).to_json()

    else:
        return f"The provided URL is unreachable | URL: {pageurl} | Status code: {response.status_code}"
