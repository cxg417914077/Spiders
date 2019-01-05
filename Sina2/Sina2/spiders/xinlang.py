# -*- coding: utf-8 -*-
import scrapy
import os
from Sina2.items import Sina2Item


class XinlangSpider(scrapy.Spider):
    name = 'xinlang'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        da_list = response.xpath('//div[@id="tab01"]/div[@class="clearfix"]/h3/a')
        for da_tag in da_list:
            da_title = da_tag.xpath('./text()').extract()[0]
            da_url = da_tag.xpath('./@href').extract()[0]
            xiao_list = response.xpath('//div[@id="tab01"]//div[@class="clearfix"]/ul/li/a')
            for xiao_tag in xiao_list:
                xiao_title = xiao_tag.xpath('./text()').extract()[0]
                xiao_url = xiao_tag.xpath('./@href').extract()[0]

                if xiao_url.startswith(da_url):
                    save_path = './data/'+da_title+'/'+xiao_title

                    if not os.path.exists(save_path):
                        os.makedirs(save_path)

                    item = Sina2Item()
                    item['xiao_title'] = xiao_title
                    item['xiao_url'] = xiao_url
                    item['da_title'] = da_title
                    item['da_url'] = da_url
                    item['save_path'] = save_path

                    meta = {'item': item}

                    yield scrapy.Request(xiao_url, callback=self.second, meta=meta)

    def second(self, response):
        item = response.meta['item']
        all_link = response.xpath('//a/@href').extract()

        for link in all_link:
            if link.startswith(item['da_title']) and link.endswith('.shtml'):
                yield scrapy.Request(link, callback=self.third, meta={'item': item})

    def third(self, response):
        item = response.meta['item']
        tiezi_title = response.xpath('//h1[@class="main-title"]/text()').extract()[0]
        tiezi_content = response.xpath('//div[@class="article"]/p/text()').extract()
        if tiezi_content:
            tiezi_content = ' '.join(tiezi_content)

        if len(tiezi_content) > 0 and len(tiezi_title):

            item['tiezi_title'] = tiezi_title
            item['tiezi_content'] = tiezi_content
            item['tiezi_url'] = response.url

            yield item

