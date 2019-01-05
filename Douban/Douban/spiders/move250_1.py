# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class Move2501Spider(scrapy.Spider):
    name = 'move250_1'
    allowed_domains = ['movie.douban.com']

    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = [url+str(offset)+"&filter="]

    def parse(self, response):
        print("resonse.url===",response.url)

        node_list = response.xpath('//div[@class="item"]')

        for node in node_list:
            title = node.xpath('.//span[@class="title"][1]/text()').extract()
            score = node.xpath('.//div[@class="star"]/span[2]/text()').extract()
            info = node.xpath('.//div[@class="info"]//p/span/text()').extract()
            if title:
                title = " ".join(title)

            if score:
                score = " ".join(score)


            if info :
                info = " ".join(info)

            item =    DoubanItem()
            item["title"] = title
            item["score"] = score
            item["info"] = info

            yield item


            #下一页
            if self.offset < 225:
                self.offset += 25

            new_next_url =  self.url+str(self.offset)+"&filter="
            yield scrapy.Request(new_next_url,callback=self.parse)



