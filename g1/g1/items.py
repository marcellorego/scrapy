# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class G1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    extraction_date = scrapy.Field()
    section = scrapy.Field()
    section_link = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    resume = scrapy.Field()     
    aggregated = scrapy.Field()
    pass