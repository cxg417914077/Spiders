# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Douban.items import DoubanItem


class Move2502Spider(CrawlSpider):
    name = 'move250_2'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=225&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print("resonse.url===", response.url)

        node_list = response.xpath('//div[@class="item"]')

        for node in node_list:
            title = node.xpath('.//span[@class="title"][1]/text()').extract()
            score = node.xpath('.//div[@class="star"]/span[2]/text()').extract()
            info = node.xpath('.//div[@class="info"]//p/span/text()').extract()
            if title:
                title = " ".join(title)

            if score:
                score = " ".join(score)

            if info:
                info = " ".join(info)

            item = DoubanItem()
            item["title"] = title
            item["score"] = score
            item["info"] = info

            yield item

