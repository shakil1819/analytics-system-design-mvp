import scrapy
from bs4 import BeautifulSoup

class WebScraper(scrapy.Spider):
    name = "web_scraper"
    start_urls = [
        'http://example.com',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for link in soup.find_all('a'):
            yield {
                'text': link.text,
                'url': link.get('href')
            }
