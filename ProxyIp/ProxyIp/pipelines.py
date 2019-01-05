# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime


class ProxyipPipeline(object):
    def open_spider(self, spider):
        date = str(datetime.now()).split(' ')[0]
        file_name = '高匿代理1'+date+'.txt'
        self.f = open(file_name, 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        a = item['host']+':'+item['port']+'\n'
        self.f.write(a)
        return item
