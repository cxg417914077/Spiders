# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dongguan.items import DongguanItem


class YangguangSpider(CrawlSpider):
    name = 'yangguang'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4'), follow=False),
        Rule(LinkExtractor(allow=r'question/\d+/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # with open('456564456654.txt', 'a', encoding='utf-8') as f:
        #     f.write(response.url+'\n')
        title_number = response.xpath(' //div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0]
        title = title_number.split('  ')[0].split('：')[1]
        number = title_number.split('  ')[1].split(':')[1]
        content = response.xpath('//div[@class="pagecenter p3"]//div[@class="c1 text14_2"]/text() | //div[@class="pagecenter p3"]//div[@class="contentext"]/text()').extract()
        if content:
            content = ' '.join(content)
        # print(content)

        item = DongguanItem()
        item['url'] = response.url
        item['title'] = title
        item['number'] = number
        item['content'] = content

        yield item