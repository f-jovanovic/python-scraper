import json


class PageData:
    def __init__(self, url, logourl, phonenumbers):
        self.URL = url
        self.logoURL = logourl
        self.phoneNumbers = phonenumbers

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
