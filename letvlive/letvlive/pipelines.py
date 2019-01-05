# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline

from letvlive.settings import IMAGES_STORE


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # return [Request(x) for x in item.get(self.images_urls_field, [])]
        yield scrapy.Request(item['screenshot'])

    def item_completed(self, results, item, info):
        # if isinstance(item, dict) or self.images_result_field in item.fields:
        #     item[self.images_result_field] = [x for ok, x in results if ok]
        image_path = [x['path'] for ok, x in results if ok][0]
        old_path = IMAGES_STORE+image_path
        new_path = IMAGES_STORE+item['nick']+'.jpg'
        os.rename(old_path, new_path)
        return item


class LetvlivePipeline(object):
    def open_spider(self, spider):
        self.f = open('letv.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # dict_item = dict(item)
        # str_item = json.dumps(dict_item, ensure_ascii=False)
        self.f.write(json.dumps(dict(item), ensure_ascii=False)+'\n')
        return item

    def close_spider(self, spider):
        self.f.close()
