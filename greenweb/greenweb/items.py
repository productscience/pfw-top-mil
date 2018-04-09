# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GreenwebItem(scrapy.Item):
    green = scrapy.Field()
    url = scrapy.Field()
    google = scrapy.Field()
    data = scrapy.Field()
    hostedby = scrapy.Field()
    hostedbyid = scrapy.Field()
    hostedbywebsite = scrapy.Field()
    partner = scrapy.Field()

