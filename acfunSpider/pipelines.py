# -*- coding: utf-8 -*-
import pymysql
from twisted.enterprise import adbapi
from .items import UserItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AcfunspiderPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            password=settings["MYSQL_PASSWORD"],
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,  # 指定 curosr 类型
            use_unicode=True,
        )
        # 指定擦做数据库的模块名和数据库参数
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    # 使用twisted将mysql插入变成异步执行
    def process_item(self, item, spider):
        if isinstance(item,UserItem):
            # 指定操作方法和操作的数据
            query = self.dbpool.runInteraction(self.user_do_insert, item)
            # 指定异常处理方法
            query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def user_do_insert(self, cursor, item):
        sel_sql = "SELECT user_id FROM user WHERE user_id = " + str(item['user_id'])
        cursor.execute(sel_sql)
        user_row = cursor.fetchone()
        if user_row:
            update_user = """
                update user set signature = %s, video_number = %s,fans_number = %s,follows_number = %s
            """
            cursor.execute(update_user, (
                 item["signature"], item["video_number"], item["fans_number"], item["follows_number"]))
            print("更新 id="+str(item['user_id']))
        else:
            insert_mysql = """
                insert into user(user_id, nick_name, signature, url, video_number, fans_number, follows_number)
                VALUE(%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_mysql, (
            item["user_id"], item["nick_name"], item["signature"], item["url"], item["video_number"], item["fans_number"],
            item["follows_number"]))
