# -*- coding: utf-8 -*-
import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['httpbin.org']
    # start_urls = ['http://httpbin.org/post']

    def start_requests(self):
        url = 'http://httpbin.org/post'
        data = {'name':'成旭光', 'age': '18'}
        yield scrapy.FormRequest(url, formdata=data, callback=self.parse)

    def parse(self, response):
        with open('post.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
