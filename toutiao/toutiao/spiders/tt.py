# -*- coding: utf-8 -*-
from toutiao.items import ToutiaoItem
import scrapy
from ASCP import get_as_cp
import re
import json
from pyquery import PyQuery as pq


class TtSpider(scrapy.Spider):
    AS, CP = get_as_cp()
    name = 'tt'
    allowed_domains = ['toutiao.com']
    base_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as='+AS+'&cp='+CP
    start_urls = [base_url]

    def parse(self, response):
        # 将json格式数据转换为字典
        text = json.loads(response.text)
        if text['message'] == 'success':
            a = re.compile('"source_url": "/group/(.*?)",')
            s = json.dumps(text, ensure_ascii=False)
            detail_urls = re.findall(a, s)
            mt = re.compile('"max_behot_time": (\d+)')
            max_behot_time = re.findall(mt, response.text)
            if max_behot_time:
                max_behot_time = ' '.join(max_behot_time)
            for detail_url in detail_urls:
                url = 'https://www.toutiao.com/a'+detail_url

                yield scrapy.Request(url, callback=self.second)
            next_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time='+max_behot_time+'&max_behot_time_tmp='+max_behot_time+'&tadrequire=true&as='+get_as_cp()['as']+'&cp='+get_as_cp()['cp']
            yield scrapy.Request(next_url, callback=self.parse)

    def second(self, response):
        item = ToutiaoItem()
        # print(response.url)
        # 文章标题
        title_re = re.compile('<title>(.*?)</title>', re.S)
        article_title = re.findall(title_re, response.text)
        if article_title:
            article_title = ''.join(article_title)
        # 文章内容
        content_re = re.compile(",\n      content: \'(.*?)',\n      groupId", re.S)
        article_content = re.findall(content_re, response.text)
        if article_content:
            article_content = article_content[0]
            article_content = article_content.replace('&lt;', '<').replace('&gt;', '>').replace('&#x3D;', '=').replace('&quot;', '"')
            # image_re = re.compile('')
            # doc = pq(article_content)
            # article_content = doc('p').text()
            # https://www.cnblogs.com/lei0213/p/7676254.html
            # print(article_content)
            # with open('detail.txt', 'a', encoding='utf-8') as f:
            #     f.write(article_content+'\n')
            item['article_url'] = response.url
            item['article_title'] = article_title
            item['article_content'] = article_content

            yield item




