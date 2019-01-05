# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # 朝向
    Direction = scrapy.Field()
    # 区域
    District = scrapy.Field()
    # 电梯
    Elevator = scrapy.Field()
    # 楼层
    Floor = scrapy.Field()
    # 花园
    Garden = scrapy.Field()
    # 链家编号
    itemid = scrapy.Field()
    # 布局 几室几厅
    Layout = scrapy.Field()
    # 价格
    Price = scrapy.Field()
    # 地区
    Region = scrapy.Field()
    # 装修风格  精装/其他
    Renovation = scrapy.Field()
    # 建筑面积
    Size = scrapy.Field()
    # 哪一年
    Year = scrapy.Field()
