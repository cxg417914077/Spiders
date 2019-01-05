# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql


class LianjiaPipeline(object):
    def open_spider(self, spider):
        # self.f = open('house2.json', 'w', encoding='utf-8')
        self.mysqlcli = pymysql.connect(host='localhost', user='root', password="guang1995",database='toutiao', port=3306,charset='utf8')

    def process_item(self, item, spider):
        # self.f.write(json.dumps(dict(item), ensure_ascii=False)+'\n')
        cur = self.mysqlcli.cursor()
        params = [item['Direction'], item['District'], item['Elevator'], item['Floor'], item['Garden'], item['itemid'], item['Layout'], item['Price'], item['Region'], item['Renovation'], item['Size'], item['Year']]
        sql = "INSERT INTO lianjia_items(Direction,District,Elevator,Floor,Garden,itemid,Layout,Price,Region,Renovation,Size,Year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, params)
        self.mysqlcli.commit()
        cur.close()
        return item

    # def close_spider(self, spider):
        # self.f.close()
