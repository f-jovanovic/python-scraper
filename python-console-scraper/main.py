import os
import sys

import requests


from executionhelper import execute_concurrently
from scraper.scarper import scrape_url

if __name__ == "__main__":
    try:
        try:
            argument = sys.argv[1]
            if not argument or argument and not argument.strip():
                raise IndexError()
        except IndexError:
            print("No valid parameter was passed.")
            sys.exit()

        if os.path.isfile(argument) and os.stat(argument).st_size != 0:
            file = open(argument, "r")
            filecontent = file.read().split("\n")
            file.close()
            execute_concurrently(scrape_url, filecontent)
        else:
            try:
                response = requests.get(argument)
                if response and response.ok:
                    scrape_url(response.text)
            except requests.RequestException:
                print("The supplied argument is not a valid URL")

    except Exception:
        print("An error has occurred")
