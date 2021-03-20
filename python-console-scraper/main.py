import os
import sys

from executionhelper import execute_concurrently
from scraper.scarper import scrape_page


def main():
    try:
        try:
            argument = sys.argv[1]
            if not argument or argument and not argument.strip():
                raise IndexError()
        except IndexError:
            print("No valid parameter was passed")
            sys.exit()

        if os.path.isfile(argument) and os.stat(argument).st_size != 0:
            file = open(argument, "r")
            filecontent = file.read().split("\n")
            file.close()
            execute_concurrently(scrape_page, filecontent)
        else:
            print(scrape_page(argument))

    except Exception as e:
        print("An error has occurred")
        print(f"Exception message: {str(e)}")


if __name__ == "__main__":
    main()
