# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ProxyIp.items import ProxyipItem


class Xici2Spider(CrawlSpider):
    name = 'xici2'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1']

    rules = (
        Rule(LinkExtractor(allow=r'nn/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ProxyipItem()
        info_list = response.xpath('//tr[@class="odd"]')
        for info in info_list:
            host = info.xpath('./td[2]/text()').extract()[0]
            port = info.xpath('./td[3]/text()').extract()[0]

            item['host'] = host
            item['port'] = port
            print(host, port)

            yield item
