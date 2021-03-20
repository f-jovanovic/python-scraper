import phonenumbers


def get_phones(html):
    if html:
        phones = []
        elements = html.find_all(["a", "p", "span", "td"])
        if elements:
            for item in elements:
                try:
                    parsed = phonenumbers.parse(item.text.strip())
                    phones.append(
                        phonenumbers.phonenumberutil.format_number(
                            parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
                        ).replace("-", "")
                    )
                except Exception:
                    None
            if phones:
                return phones
