# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class A66dailiSpider(CrawlSpider):
    name = '66daili'
    allowed_domains = ['66ip.cn']
    start_urls = ['http://www.66ip.cn/2.html']

    rules = (
        Rule(LinkExtractor(allow=r'cn/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        a = re.compile('\d+.\d+.\d+.\d+')
        ip_list = a.findall(response.text)
        print(ip_list)
