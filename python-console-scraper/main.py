import os
import sys

from executionhelper import execute_concurrently
from scraper.scraper import scrape_page


def main():
    try:
        try:
            print(
                "Enter page URLs separated into new lines (press CTRL+D to finish inputing): "
            )
            arguments = sys.stdin.readlines()
            if not arguments:
                raise IndexError()
        except IndexError:
            print("No valid parameter was passed")
            sys.exit()

        if arguments.__len__():
            execute_concurrently(scrape_page, arguments)

    except Exception as e:
        print("An error has occurred")
        print(f"Exception message: {str(e)}")


if __name__ == "__main__":
    main()
