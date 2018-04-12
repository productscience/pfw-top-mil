import json
import scrapy


# import ipdb; ipdb.set_trace()

from greenweb.domain_generator import gen_urls


class GreenOrNotSpider(scrapy.Spider):
    name = "green_or_not"

    def start_requests(self):
        
        tag = getattr(self, 'tag', None)
        # exit early if we don't have an integer as our tag
        assert type(tag) == int

        file_path = 'top-{}-subsection.csv'.format(tag)


        with open(file_path) as csvfile:

            urls = gen_urls(csvfile)

            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        site = json.loads(response.body)
        yield site