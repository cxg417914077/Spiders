# -*- coding: utf-8 -*-
import scrapy

from Dongguan1.items import Dongguan1Item


class Yangguang2Spider(scrapy.Spider):
    offset = 0
    name = 'yangguang2'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='

    def parse_item(self, response):
        title_number = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0]
        title = title_number.split('  ')[0].split('：')[1]
        number = title_number.split('  ')[1].split(':')[1]
        content = response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
        if content:
            content = ' '.join(content)

        item = Dongguan1Item()
        item['title'] = title
        item['number'] = number
        item['content'] = content

        yield item

    def parse(self, response):
        for link in response.xpath('//a[@class="news14"]/@href').extract():
            yield scrapy.Request(link, callback=self.parse_item)

        if self.offset < 101520:
            self.offset += 1
            next_url = self.url + str(self.offset)
            yield scrapy.Request(next_url, callback=self.parse)
