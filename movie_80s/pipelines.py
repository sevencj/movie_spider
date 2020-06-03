# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi


class Movie80SPipeline(object):
    # def __init__(self):
    #     self.f = open('movies_80s.json', 'w', errors='ignore')
    #
    # def process_item(self, item, spider):
    #     content = json.dumps(dict(item), ensure_ascii=False)
    #     self.f.write(content + '\n\n')
    #     return item
    #
    # def close_spider(self, spider):
    #     self.f.close()

    def __init__(self, dbpool):
        # connection database
        self.dbpool = dbpool
        # self.connect = pymysql.connect(host='localhost',
        #                                user='root',
        #                                passwd='scorpiocheng123',
        #                                db='movie_80s',
        #                                charset='utf8')  # 后面三个依次是数据库连接名、数据库密码、数据库名称
        # # get cursor
        # self.cursor = self.connect.cursor()
        # print("连接数据库成功")

    @classmethod
    def from_settings(cls, settings):
        params = dict(

            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset=settings['MYSQL_CHARSET'],
            port=settings['MYSQL_PORT'],
            cursorclass=cursors.DictCursor,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **params)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.insert_db, item)
        query.addErrback(self.handle_error)
        return item

        # # sql语句
        # insert_sql = r'insert into movie(mname, mimg, mdesc, mlink) VALUES(%s,%s,%s,%s)'
        #
        # # 执行插入数据到数据库操作
        # self.cursor.execute(insert_sql, (item['name'], item['img'], item['desc'], item['link']))
        # # 提交，不进行提交无法保存到数据库
        # self.connect.commit()

    def handle_error(self, field):
        print('-----数据库写入失败：', field)

    def insert_db(self, cursor, item):
        insert_sql = r'insert into movie(mname, mimg, mdesc, mlink) VALUES(%s,%s,%s,%s)'
        cursor.execute(insert_sql, (item['name'], item['img'], item['desc'], item['link']))


    # def close_spider(self, spider):
    #     # 关闭游标和连接
    #     self.cursor.close()
    #     self.connect.close()

