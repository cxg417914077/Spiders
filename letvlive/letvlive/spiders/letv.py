# -*- coding: utf-8 -*-
import scrapy
import json
from letvlive.items import LetvliveItem

class LetvSpider(scrapy.Spider):
    name = 'letv'
    allowed_domains = ['m.letv.com']
    pre_url = 'http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&channelId=1663&pcode=010110174&version=8.6&pages='
    page = 1
    sub_url = '&country=CN&provinceid=1&districtid=17&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%98%8C%E5%B9%B3%E5%8C%BA%7C%E6%B2%99%E6%B2%B3%E9%95%87&region=CN&lang=chs'
    start_urls = [pre_url+str(page)+sub_url]

    def parse(self, response):
        data = json.loads(response.text, encoding='utf-8')
        for node in data['body']['result']:
            nick = node['nick']
            liveUrl = node['liveUrl']
            screenshot = node['screenshot']

            item = LetvliveItem()
            item['nick'] = nick
            item['liveUrl'] = liveUrl
            item['screenshot'] = screenshot

            yield item

            if self.page < 10:
                self.page += 1
                next_url = self.pre_url+str(self.page)+self.sub_url
                yield scrapy.Request(next_url, callback=self.parse)
