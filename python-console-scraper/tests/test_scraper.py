from scraper.scraper import scrape_page


def test_scraper_invalid_url():
    invalid_url = "test"
    assert scrape_page(invalid_url) == f"The URL is invalid | URL: {invalid_url}"


def test_scraper_status_code_not_ok():
    page_url = "https://www.amazon.com"
    assert (
        scrape_page(page_url)
        == f"The provided URL is unreachable | URL: {page_url} | Status code: 503"
    )
