# -*- coding: utf-8 -*-
import scrapy


class Rrlogin2Spider(scrapy.Spider):
    name = 'rrlogin2'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/']

    def parse(self, response):
        data = {'email': '15731664508', 'password': 'guang1995'}
        yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.abc)

    def abc(self, response):
        with open('my.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        yield scrapy.Request('http://www.renren.com/410057922/profile', callback=self.lcz)

    def lcz(self, response):
        with open('lcz.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
