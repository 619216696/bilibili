# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_ = scrapy.Field()
    following = scrapy.Field()
    fans = scrapy.Field()
    play_num = scrapy.Field()
    uid = scrapy.Field()
    reg_time = scrapy.Field()
    birthday = scrapy.Field()
    area = scrapy.Field()
    sex = scrapy.Field()
    coins = scrapy.Field()
    article = scrapy.Field()
    exp = scrapy.Field()
    level_ = scrapy.Field()
    description = scrapy.Field()
    pass
