# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class AcfunspiderItem(Item):
    pass

class UserItem(Item):
    user_id = Field()
    nick_name = Field()
    url = Field()
    video_number = Field()
    fans_number = Field()
    follows_number = Field()
    signature = Field()

class VideoItem(Item):
    title = Field()
    data_url = Field()
    watch_number = Field()
    barrage_number = Field()
    time = Field()
