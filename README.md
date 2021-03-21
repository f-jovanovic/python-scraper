# python-scraper
A .py project for scraping website logos and phone number

## Building a docker image
To create a docker container with your application use 
```
sudo docker build -t image_name --rm .
```

## Running the application with Docker
After creating a docker image you can run the application like this:
```
sudo docker run -i image_name
```
Although this will work, no instructions for parameter entry will print on the screen.
To run the application interactively and get the input instructions printed you can run:
```
sudo docker run -it image_name
```

This will make the application print the instructions first, before waiting for input.
Alternatively, if you want to send contents of a file (ex. using the cat command) as an argument you will need to use the -i flag:
```
cat file_path | sudo docker run -t image_name
```

## Parameters
The expected input is a list of strings, formatted like a full URL(https://www.something.com/etc).

## Technical overview

### Scraper
This program uses the BeautifulSoup library for scraping elements from a webpage.

All valid input arguments are passed into the execute_concurrently function, which creates a thread executing the scrape_page function for each argument (the maximum number of threads is determined by the futures library, although it can also be set).

The logo scraper currently covers 5 possible matches for a logo element, iterating through them until one of the cases returns a result.
The execution starts with the highest possible chance of an image being a match, to the lowest.
It iterates through each tag looking for an img element with a source URL, returning it if it's found.
All relative URLs are converted to absolute.

Phone scraping is done by using regex to match any elements that are in a list.
The matched phone numbers are also cleaned using a different regex pattern.

After scraping for logos and numbers, the results are passed into a new PageData object, which is then serialized to JSON and printed to the console.

### Unit tests
The tests folder contains unit tests for the functions that are used.
To run them you need to install pytest, and then go to the root directory and run `pytest`.
