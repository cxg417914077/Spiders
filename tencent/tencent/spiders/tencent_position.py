# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem


class TencentPositionSpider(CrawlSpider):
    name = 'tencent_position'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?lid=&tid=&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start=10#a']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for node in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            position_name = node.xpath('./td[1]/a/text()').extract()[0]
            position_cate = node.xpath('./td[2]/text()').extract()
            if position_cate:
                ''.join(position_cate)
            number = node.xpath('./td[3]/text()').extract()[0]
            city = node.xpath('./td[4]/text()').extract()[0]
            public_time = node.xpath('./td[5]/text()').extract()[0]

            item = TencentItem()
            item['position_name'] = position_name
            item['position_cate'] = position_cate
            item['number'] = number
            item['city'] = city
            item['public_time'] = public_time

            yield item
