FROM python:3.8.6
COPY ./python-console-scraper/ ./python-console-scraper/
WORKDIR ./python-console-scraper/
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "/python-console-scraper/main.py"]
