import requests

from classes.pagedata import PageData


def scrape_url(pageurl):
    response = requests.get(pageurl)
    return PageData(pageurl, None, None).to_json()
