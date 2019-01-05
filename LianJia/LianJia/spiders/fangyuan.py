# -*- coding: utf-8 -*-
import scrapy
from LianJia.items import LianjiaItem


class FangyuanSpider(scrapy.Spider):

    name = 'fangyuan'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']

    def parse(self, response):
        self.detail_link = open('获取到的详情页链接.json', 'w', encoding='utf-8')
        self.detail_response_link = open('响应的详情页链接.json', 'w', encoding='utf-8')
        # 匹配的各个地区标签
        region_list = response.xpath('//div[@class="sub_nav section_sub_nav"]/a[not(contains(@href,"lf.lianjia"))]')

        # 遍历然后对网址进行拼串, 获得每个区域的链接,然后请求
        for region in region_list:
            region_url = 'https://bj.lianjia.com'+region.xpath('./@href').extract()[0]
            region_name = region.xpath('./text()').extract()[0]
            # print(region_url, region_name)
            yield scrapy.Request(region_url, callback=self.second)

    def second(self, response):
        # 获取详细区域的半截链接
        district_list = response.xpath('//div[@class="sub_sub_nav section_sub_sub_nav"]/a/@href').extract()
        # 获取每个半截链接，拼成完整链接，然后请求
        for district in district_list:
            district_url = 'https://bj.lianjia.com'+district
            yield scrapy.Request(district_url, callback=self.third)

    def third(self, response):
        # 详细区域的首页
        url = response.url
        # 判断一共有多少页
        # 先判断一共有多少套房源， 一个可以展示30套， 对房源数取整取余求出页数
        house_number = int(response.xpath('//h2[@class="total fl"]/span/text()').extract()[0])
        # with open('区域及房子数.txt', 'a', encoding='utf-8') as f:
        #     f.write(url+'----'+str(house_number)+'\n')

        # 有余数时，页数等于商加上1； 没有余数时，页数就等于商
        if house_number%30:
            page = house_number//30 + 1
        else:
            page = house_number//30
        # 当page为0时，房源只有一页或者没有，然后直接请求url数据并解析
        if page == 0:
            # print('------------------------------------')
            # print(url)
            yield scrapy.Request(url, callback=self.list)
        else:
            # page不为0时, 第一页请求url并解析，剩下的拼成完整地址然后请求并解析
            for pg in range(1, page+1):
                # 第一页
                if pg == 1:
                    yield scrapy.Request(url, callback=self.list)
                else:
                    # 其余页
                    new_url = url+'pg'+str(pg)+'/'
                    # print('++++++++++++++++++++++++++++++++++++++++')
                    # print(new_url)
                    yield scrapy.Request(new_url, callback=self.list)

    def list(self, response):
        # 获取每个详情页的网址，存在就请求然后解析
        detail_list = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        for detail_url in detail_list:
            if detail_url:
                self.detail_link.write(detail_url+'\n')
                yield scrapy.Request(detail_url, callback=self.info)

        # print(house_number, response.url)
        # for detail_url in detail_list:
        #     # with open('url.txt', 'a', encoding='utf-8') as f:
        #     #     f.write(detail_url+'\n')
        #     yield scrapy.Request(detail_url, callback=self.info)
        #
        #     if self.pg < 100:
        #         self.pg += 1
        #         next_url = 'https://bj.lianjia.com/ershoufang/'+'pg'+str(self.pg)
        #         yield scrapy.Request(next_url, callback=self.parse)

    def info(self, response):
        self.detail_response_link.write(response.url+'\n')
        # 朝向
        Direction = response.xpath('//div[@class="type"]/div[@class="mainInfo"]/text()').extract()
        if Direction:
            Direction = ' '.join(Direction)

        # 区域
        District = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[2]/text()').extract()
        if District:
            District = ' '.join(District)

        # 有无电梯
        Elevator = response.xpath('//div[@class="content"]/ul/li[12]/text()').extract()
        if Elevator:
            Elevator = ' '.join(Elevator)

        # 所在楼层
        Floor = response.xpath('//div[@class="content"]/ul/li[2]/text()').extract()
        if Floor:
            Floor = ' '.join(Floor).replace('\n', '').replace(' ', '')

        # 小区
        Garden = response.xpath('//div[@class="communityName"]/a[1]/text()').extract()
        if Garden:
            Garden = ' '.join(Garden)

        # 链家编号
        Id = response.xpath('//div[@class="houseRecord"]/span[@class="info"]/text()').extract()
        if Id:
            Id = ' '.join(Id)

        # 几室几厅
        Layout = response.xpath('//div[@class="content"]/ul/li[1]/text()').extract()
        if Layout:
            Layout = ' '.join(Layout).replace('\n', '').replace(' ', '')

        # 价格
        Price = response.xpath('//div[@class="price"]/span[@class="total"]/text()|//div[@class="price "]/span[@class="total"]/text()').extract()
        if Price:
            Price = ' '.join(Price)

        # 地区
        Region = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[1]/text()').extract()
        if Region:
            Region = ' '.join(Region)

        # 装修风格  精装/其他
        Renovation = response.xpath('//div[@class="content"]/ul/li[9]/text()').extract()
        if Renovation:
            Renovation = ' '.join(Renovation)

        # 建筑面积
        Size = response.xpath('//div[@class="content"]/ul/li[3]/text()').extract()
        if Size:
            Size = ' '.join(Size).replace('\n', '').replace(' ', '')

        # 哪一年建楼
        Year = response.xpath('//div[@class="area"]/div[@class="subInfo"]/text()').extract()
        if Year:
            Year = ' '.join(Year)

        item = LianjiaItem()
        item['Direction'] = Direction
        item['District'] = District
        item['Elevator'] = Elevator
        item['Floor'] = Floor
        item['Garden'] = Garden
        item['itemid'] = Id
        item['Layout'] = Layout
        item['Price'] = Price
        item['Region'] = Region
        item['Renovation'] = Renovation
        item['Size'] = Size
        item['Year'] = Year

        yield item
