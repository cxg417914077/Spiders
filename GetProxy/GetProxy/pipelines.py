# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GetproxyPipeline(object):
    def open_spider(self, spider):
        self.f = open('代理ip.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(item['url'])
        return item

    def close_spider(self, spider):
        self.f.close()
