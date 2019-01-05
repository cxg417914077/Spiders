# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from LianJia.items import LianjiaItem


class Fangyuan2Spider(CrawlSpider):
    name = 'fangyuan2'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']

    rules = (
        Rule(LinkExtractor(allow=r'bj.lianjia.com/ershoufang/'), follow=True),
        Rule(LinkExtractor(allow=r'bj.lianjia.com/ershoufang/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 朝向
        Direction = response.xpath('//div[@class="type"]/div[@class="mainInfo"]/text()').extract()[0]
        # 区域
        District = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[2]/text()').extract()[0]
        # 有无电梯
        Elevator = response.xpath('//div[@class="content"]/ul/li[12]/text()').extract()[0]
        # 所在楼层
        Floor = response.xpath('//div[@class="content"]/ul/li[2]/text()').extract()[0]
        # 小区
        Garden = response.xpath('//div[@class="communityName"]/a[1]/text()').extract()[0]
        # 链家编号
        Id = response.xpath('//div[@class="houseRecord"]/span[@class="info"]/text()').extract()[0]
        # 几室几厅
        Layout = response.xpath('//div[@class="content"]/ul/li[1]/text()').extract()[0]
        # 价格
        Price = response.xpath(
            '//div[@class="price"]/span[@class="total"]/text()|//div[@class="price "]/span[@class="total"]/text()').extract()[
            0]
        # 地区
        Region = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[1]/text()').extract()[0]
        # 装修风格  精装/其他
        Renovation = response.xpath('//div[@class="content"]/ul/li[9]/text()').extract()[0]
        # 建筑面积
        Size = response.xpath('//div[@class="content"]/ul/li[5]/text()').extract()[0]
        # 哪一年建楼
        Year = response.xpath('//div[@class="area"]/div[@class="subInfo"]/text()').extract()[0]

        item = LianjiaItem()
        item['Direction'] = Direction
        item['District'] = District
        item['Elevator'] = Elevator
        item['Floor'] = Floor
        item['Garden'] = Garden
        item['Id'] = Id
        item['Layout'] = Layout
        item['Price'] = Price
        item['Region'] = Region
        item['Renovation'] = Renovation
        item['Size'] = Size
        item['Year'] = Year

        yield item

