# -*- coding: utf-8 -*-
import pymysql
from twisted.enterprise import adbapi
from .items import UserItem, VideoItem


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AcfunspiderPipeline(object):

    def process_item(self, item, spider):
        db = pymysql.connect(user="root", passwd="123456", db="acfun", host="127.0.0.1", port=int(3306),
                             charset="utf8", use_unicode=True)
        if isinstance(item, UserItem):
            self.user_do_insert(db, item)
        if isinstance(item, VideoItem):
            self.video_do_insert(db, item)

    def user_do_insert(self, db, item):
        cursor = db.cursor()
        sel_sql = "SELECT user_id FROM user WHERE user_id = " + str(item['user_id'])
        cursor.execute(sel_sql)
        user_row = cursor.fetchone()
        if user_row:
            update_user = """
                update user set signature = %s, video_number = %s,fans_number = %s,follows_number = %s
            """
            cursor.execute(update_user, (
                item["signature"], item["video_number"], item["fans_number"], item["follows_number"]))
            db.commit()
            cursor.close()
        else:
            insert_mysql = """
                insert into user(user_id, nick_name, signature, url, video_number, fans_number, follows_number)
                VALUE(%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_mysql, (
                item["user_id"], item["nick_name"], item["signature"], item["url"], item["video_number"],
                item["fans_number"],
                item["follows_number"]))
            db.commit()
            cursor.close()

    def video_do_insert(self, db, item):
        cursor = db.cursor()
        sel_video_sql = "SELECT data_url FROM video WHERE data_url = '" + str(item['data_url']) + "'"
        cursor.execute(sel_video_sql)
        video_row = cursor.fetchone()
        if video_row:
            update_video = """update video set watch_number = %s, barrage_number = %s"""
            cursor.execute(update_video, (int(item["watch_number"]), int(item["barrage_number"])))
            cursor.close()
            db.commit()
        else:
            insert_video_mysql = """
                        insert into video(user_id, title, data_url, watch_number, barrage_number,time)
                        VALUE(%s, %s, %s, %s, %s,%s)"""
            cursor.execute(insert_video_mysql, (
                int(item["user_id"]), item["title"], item["data_url"], item["watch_number"],
                item["barrage_number"], item['time']))
            cursor.close()
            db.commit()
