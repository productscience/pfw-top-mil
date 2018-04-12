import json
import scrapy
from pathlib import Path


from greenweb.domain_generator import (gen_urls, fetch_top_mil,
                                       decompress_top_mil, cut_down_list)


class GreenOrNotSpider(scrapy.Spider):
    name = "green_or_not"

    def start_requests(self):

        tag = getattr(self, 'tag', None)
        assert type(tag) is not None
        # exit early if we don't have an integer as our tag
        assert int(tag)

        file_path = 'top-{}-subsection.csv'.format(tag)

        if not Path(file_path).exists():
            fetch_top_mil()
            decompress_top_mil('top-1m.csv.zip')
            cut_down_list(int(tag), 'top-1m.csv')

        with open(file_path) as csvfile:

            urls = gen_urls(csvfile)

            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        site = json.loads(response.body)
        yield site