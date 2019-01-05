# -*- coding: utf-8 -*-
import scrapy, json, re
from tmall.items import TmallItem


class XiongzhaoSpider(scrapy.Spider):
    name = 'xiongzhao2'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E7%BD%A9&psort=3&click=0']

    def parse(self, response):
        url_list = response.xpath('//ul[@class="gl-warp clearfix"]//div[@class="p-img"]/a[@target="_blank"]/@href').extract()
        for url in url_list:
            itemid = url.replace('//item.jd.com/', '').replace('.html', '')
            pages_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv6986&productId='+str(itemid)+'&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
            yield scrapy.Request(pages_url, callback=self.second, meta={'itemid': itemid, 'download_timeout': 10})

    def second(self, response):
        itemid = response.meta['itemid']
        text = response.text
        a = re.compile(r'fetchJSON_comment98vv\d{4}\(')
        b = re.findall(a, text)[0]
        text = text.replace(b, '').replace(');', '')
        text = json.loads(text, encoding='utf-8')
        pagination = int(text['maxPage'])
        for currentPage in range(int(pagination)):
            detail_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv6986&productId='+str(itemid)+'&score=0&sortType=5&page='+str(currentPage)+'&pageSize=10&isShadowSku=0&rid=0&fold=1'
            yield scrapy.Request(detail_url, callback=self.third, meta={'download_timeout': 10})

    def third(self, response):
        text = response.text
        a = re.compile(r'fetchJSON_comment98vv\d{4}\(')
        b = re.findall(a, text)[0]
        text = text.replace(b, '').replace(');', '')
        text = json.loads(text, encoding='utf-8')
        rateList = text['comments']
        for rate in rateList:
            color = rate['productColor']
            size = rate['productSize']
            date = rate['creationTime']
            comment = rate['content']
            source = '京东'
            item = TmallItem()
            item['color'] = color
            item['size'] = size
            item['date'] = date
            item['comment'] = comment
            item['source'] = source
            yield item


