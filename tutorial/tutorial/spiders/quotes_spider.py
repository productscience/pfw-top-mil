import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text' : quote.css("span.text::text").extract_first(),
                'author' : quote.css('small.author::text').extract_first(),
                'tags' : quote.css('div.tags a.tag::text').extract()
            }

        for a in response.css('li.next a')
            yield response.follow(a, callback=self.parse)
