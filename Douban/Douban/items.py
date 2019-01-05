# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    #
    # 电影标题: title
    title = scrapy.Field()
    # 电影的评分: score
    score = scrapy.Field()
    # 电影一句话信息：info
    info = scrapy.Field()
