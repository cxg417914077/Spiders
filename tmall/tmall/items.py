# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallItem(scrapy.Item):
    # define the fields for your item here like:
    color = scrapy.Field()
    size = scrapy.Field()
    date = scrapy.Field()
    comment = scrapy.Field()
    source = scrapy.Field()
