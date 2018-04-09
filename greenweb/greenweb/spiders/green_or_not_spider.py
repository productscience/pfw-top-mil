import scrapy
import json

class GreenOrNotSpider(scrapy.Spider):
    name = "green_or_not"

    def start_requests(self):
        urls = [
            'http://api.thegreenwebfoundation.org/greencheck/google.com',
            'http://api.thegreenwebfoundation.org/greencheck/youtube.com',
            'http://api.thegreenwebfoundation.org/greencheck/facebook.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        site = json.loads(response.body)
        yield site