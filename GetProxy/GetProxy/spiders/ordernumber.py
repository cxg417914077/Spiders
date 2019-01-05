# -*- coding: utf-8 -*-
import scrapy
from GetProxy.items import GetproxyItem
import random


class OrdernumberSpider(scrapy.Spider):
    name = 'ordernumber'
    allowed_domains = ['api3.xiguadaili.com']
    start_urls = ['http://api3.xiguadaili.com/ip/?tid=555805581351464&num=20']

    def parse(self, response):
        item = GetproxyItem()
        url = 'http://api3.xiguadaili.com/ip/?tid='+'55'+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+'&num=20'
        content = response.text
        if content.startswith('ERROR|'):
            print(content)
            print(url)
            yield scrapy.Request(url, callback=self.parse)
        else:
            item['url'] = response.url
            yield item

