from bs4 import BeautifulSoup

import scraper.logoscraper as logoscraper

test_base_url = "https://www.testbase.com"


def test_get_logo_should_pass():
    htmls = [
        f"<div class='logo'><img src='https://www.test.com'></img></div>",
        f"<div id='logo'><img src='https://www.test.com'></img></div>",
        f"<a><img src='https://www.test.com'></img></a>",
        f"<div><img src='https://www.test.com'></img></div>",
        f"<a href={test_base_url}><img src='https://www.test.com'></img></div>",
    ]
    for html in htmls:
        assert (
            logoscraper.get_logo(BeautifulSoup(html, "html.parser"), test_base_url)
            == "https://www.test.com"
        )


def test_find_image_tag():
    result = logoscraper.find_img_tag(
        BeautifulSoup(
            f'<a><img src="https://{test_base_url}"></img></a>', "html.parser"
        ),
        test_base_url,
    )
    assert result


def test_find_image_tag_return_itself():
    result = logoscraper.find_img_tag(
        BeautifulSoup(f'<img src="https://{test_base_url}"></img>', "html.parser"),
        test_base_url,
    )
    assert result


def test_find_image_tag_retrun_none():
    result = logoscraper.find_img_tag(
        BeautifulSoup(f'<a href="https://{test_base_url}"></a>', "html.parser"),
        test_base_url,
    )
    assert result is None


def test_format_image_source():
    html = BeautifulSoup(f"<img src='{test_base_url}'></img>", "html.parser").find(
        "img"
    )
    assert logoscraper.format_image_source(html, test_base_url) == test_base_url


def test_format_image_source_no_source():
    html = BeautifulSoup(f"<img></img>", "html.parser").find("img")
    assert logoscraper.format_image_source(html, test_base_url) is None


def test_format_image_source_relative_path():
    html = BeautifulSoup(
        f"<img src='resources/images/image.png'></img>", "html.parser"
    ).find("img")
    assert (
        logoscraper.format_image_source(html, test_base_url)
        == f"{test_base_url}/resources/images/image.png"
    )
