# -*- coding: utf-8 -*-
import scrapy


class RrloginSpider(scrapy.Spider):
    name = 'rrlogin'
    allowed_domains = ['www.renren.com']
    # start_urls = ['http://www.renren.com/PLogin.do']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {
            'email': '15731664508',
            'password': 'guang1995'
        }
        yield scrapy.FormRequest(url, formdata=data, callback=self.parse)

    def parse(self, response):
        with open('rrloin1.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
