import json
import scrapy

from domain_generator import gen_urls


class GreenOrNotSpider(scrapy.Spider):
    name = "green_or_not"

    def start_requests(self):

        with open('top-50.csv') as csvfile:

            urls = gen_urls(csvfile)

            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        site = json.loads(response.body)
        yield site
