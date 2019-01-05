# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Sina2Item(scrapy.Item):
    # define the fields for your item here like:
    da_title = scrapy.Field()
    da_url = scrapy.Field()
    xiao_title = scrapy.Field()
    xiao_url = scrapy.Field()
    save_path = scrapy.Field()
    tiezi_title = scrapy.Field()
    tiezi_content = scrapy.Field()
    tiezi_url = scrapy.Field()

