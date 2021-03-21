import re


def get_phones(html):
    if html:
        phone_regex = re.compile(
            r"\(?\+?\d{1,3}\)?[\ \-\/]?\d{2,4}[\ \-\/]?\d{2,4}[\ \-\/]?\d{2,4}"
        )
        replace_pattern = re.compile(r"[/\-.]")
        phone_numbers = []
        elements = html.find_all(["a", "p", "span", "td", "div"])
        if elements:
            for item in elements:
                try:
                    number = phone_regex.search(item.text).group().strip()
                    if number and number.__len__() >= 8:
                        number = re.sub(replace_pattern, " ", number)
                        if number not in phone_numbers:
                            phone_numbers.append(number)

                except Exception:
                    None

            if phone_numbers:
                return phone_numbers
