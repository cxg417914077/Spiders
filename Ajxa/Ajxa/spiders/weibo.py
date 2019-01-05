# -*- coding: utf-8 -*-
import json
from pyquery import PyQuery as pq
import scrapy


class WeiboSpider(scrapy.Spider):
    base_url = 'https://m.weibo.cn/api/container/getIndex?display=0&retcode=6102&type=uid&value=2830678474&containerid=1076032830678474&page='
    offset = 2
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = [base_url+str(offset)]

    def parse(self, response):
        a = json.loads(response.text)
        # print(type(a))
        articles = a['data']['cards']
        # print(type(articles))
        for article in articles:
            # print(article)
            # print(type(article))
            # text = article['mblog']['text']
            text = pq(article['mblog']['text']).text()
            print(text)



