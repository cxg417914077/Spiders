# -*- coding: utf-8 -*-
import scrapy


class XiciSpider(scrapy.Spider):
    offset = 1
    name = 'xici'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1']

    def parse(self, response):
        info_list = response.xpath('//tr[@class="odd"]')
        for info in info_list:
            host = info.xpath('./td[2]/text()').extract()[0]
            port = info.xpath('./td[3]/text()').extract()[0]

            print(host,port)
        # with open('xici.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)