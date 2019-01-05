# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3, os


class TmallPipeline(object):
    def open_spider(self, spider):
        path = 'bra2.sqlite'
        if os.path.exists(path):
            os.remove(path)
        self.conn = sqlite3.connect(path)
        sql = '''
            create table sales(
           id integer primary key autoincrement not null,
           color text not null,
           size text not null,
           source text not null,
           comment text not null,
           date text not null)
        '''
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def process_item(self, item, spider):
        color = item['color']
        size = item['size']
        date = item['date']
        comment = item['comment']
        source = item['source']
        sql1 = "insert into sales(color,size,source,comment,date) values('%s','%s','%s','%s','%s');" % (
        color, size, source, comment, date)
        cur = self.conn.cursor()
        cur.execute(sql1)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
