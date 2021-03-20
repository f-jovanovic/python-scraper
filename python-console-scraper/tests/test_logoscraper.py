from bs4 import BeautifulSoup

from scraper.logoscraper import get_logo

testHTML = "<div class='logo'><img src='https://www.test.com'></img></div>"
testHTML2 = "<div id='logo'><img src='https://www.test.com'></img></div>"
testHTML3 = "<div><img src='https://www.testlogo.com'></img></div>"
testHTML4 = "<a href='www.testbase.com'><img src='https://www.test.com'></img></div>"


def test_get_logo_class():
    assert get_logo(BeautifulSoup(testHTML, "html.parser"), "www.testbase.com") == "https://www.test.com"


def test_get_logo_id():
    assert get_logo(BeautifulSoup(testHTML2, "html.parser"), "www.testbase.com") == "https://www.test.com"


def test_get_logo_src():
    assert get_logo(BeautifulSoup(testHTML3, "html.parser"), "www.testbase.com") == "https://www.testlogo.com"


def test_get_logo_href():
    assert get_logo(BeautifulSoup(testHTML4, "html.parser"), "www.testbase.com") == "https://www.test.com"

