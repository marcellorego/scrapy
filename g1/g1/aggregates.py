# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class G1AggregatedItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    pass