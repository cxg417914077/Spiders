# -*- coding: utf-8 -*-
import scrapy
from Sina.items import SinaItem


class XinlangSpider(scrapy.Spider):
    name = 'xinlang'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        item = SinaItem()

        parent_list = response.xpath('//div[@id="tab01"]/div[@class="clearfix"]/h3[@class="tit02"]/a')
        for parent in parent_list:
            parent_url = parent.xpath('./@href').extract()[0]
            parent_title = parent.xpath('./text()').extract()[0]

            item['parent_url'] = parent_url
            item['parent_title'] = parent_title

            sub_list = response.xpath('//div[@id="tab01"]/div[@class="clearfix"]/ul/li/a')
            for sub in sub_list:
                sub_url = sub.xpath('./@href').extract()[0]
                sub_title = sub.xpath('./text()').extract()[0]

                item['sub_url'] = sub_url
                item['sub_title'] = sub_title

                if sub_url.startswith(parent_url):
                    save_path = './data/'+parent_title+'/'+sub_title+'/'

                    item['save_path'] = save_path

                yield scrapy.Request(sub_url, callback=self.second, meta={'item': item})

    def second(self, response):
        item = response.meta['item']
        parent_url = item['parent_url']
        tiezi_list = response.xpath('//a/@href').extract()
        for tiezi_url in tiezi_list:
            if tiezi_url.startswith(parent_url) and tiezi_url.endswith('.shtml'):
                item['tiezi_url'] = tiezi_url

                yield scrapy.Request(tiezi_url, callback=self.third, meta={'item': item})

    def third(self, response):
        tiezi_title = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
        content_list = response.xpath('//div[@id="artibody"]/p')
        for content in content_list:
            print(content)




