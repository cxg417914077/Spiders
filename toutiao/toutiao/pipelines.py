# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ToutiaoPipeline(object):
    def open_spider(self, spider):
        self.mysqlcli = pymysql.connect(host='localhost', user='root', password="guang1995",database='toutiao', port=3306, charset='utf8')

    def process_item(self, item, spider):
        cur = self.mysqlcli.cursor()
        params = [item['article_url'], item['article_title'], item['article_content']]
        # article_url = item['article_url']
        # article_title = item['article_title']
        # article_content = item['article_content']
        sql = "INSERT INTO toutiao_items(article_url,article_title,article_content) VALUES (%s, %s, %s )"
        cur.execute(sql, params)
        self.mysqlcli.commit()
        cur.close()
        return item
