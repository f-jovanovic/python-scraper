from bs4 import BeautifulSoup

from scraper.phonescraper import get_phones


def test_get_phones_no_html():
    test_html = ""
    assert get_phones(BeautifulSoup(test_html, "html.parser")) is None


def test_get_phones_not_html():
    test_html = "test string"
    assert get_phones(BeautifulSoup(test_html, "html.parser")) is None


def test_get_phones_tag_types():
    test_htmls = [
        "<div>091 51 222 50</div>",
        "<p>091 51 222 50</p>",
        "<a>091 51 222 50</a>",
        "<span>091 51 222 50</span>",
        "<td>091 51 222 50</td>",
    ]
    for html in test_htmls:
        assert get_phones(BeautifulSoup(html, "html.parser")).__len__() == 1
        assert "091 51 222 50" in get_phones(BeautifulSoup(html, "html.parser"))


def test_get_phones_number_formats():
    test_numbers = [
        "(385) 915 122 250",
        "(385)915122250",
        "(+385) 91 51 22250",
        "+385 91 51 22 250",
        "+385915122250",
        "+385 91 51 222 50",
        "091 51222 50",
        "09151 22250",
        "09151222 50",
    ]
    for number in test_numbers:
        html = f"<a>{number}</a>"
        assert get_phones(BeautifulSoup(html, "html.parser")).__len__() == 1
        assert number in get_phones(BeautifulSoup(html, "html.parser"))


def test_get_phones_replace_chars():
    test_number = "091 51 222 50"
    numbers_to_replace = [
        test_number.replace(" ", "-"),
        test_number.replace(" ", "/"),
    ]
    for number in numbers_to_replace:
        html = f"<a>{number}</a>"
        assert get_phones(BeautifulSoup(html, "html.parser")).__len__() == 1
        assert test_number in get_phones(BeautifulSoup(html, "html.parser"))


def test_get_phones_multiple():
    numbers = ["+385 91 51 222 50", "(+385) 91 5122 250", "0915122250"]
    test_html = f"<html><div>{numbers[0]}<a>{numbers[1]}</a><span>{numbers[2]}</span></div></html>"

    result = get_phones(BeautifulSoup(test_html, "html.parser"))

    assert result
    assert result.__len__() == 3
    for number in numbers:
        assert number in result
