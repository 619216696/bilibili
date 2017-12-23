# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from bilibili.items import BilibiliItem
from bilibili.mysql import sql

class BilibiliPipeline(object):
    def process_item(self, item, spider):
        uid = item['uid']
        name_ = item['name_']
        play_num = item['play_num']
        sex = item['sex']
        birthday = item['birthday']
        area = item['area']
        reg_time = item['reg_time']
        coins = item['coins']
        article = item['article']
        level_ = item['level_']
        exp = item['exp']
        description = item['description']
        fans = item['fans']
        following = item['following']
        sql.insert_data(name_,uid,play_num,sex,birthday,area,reg_time,coins,article,level_,exp,description,fans,following)
        print('已抓取bilibili用户信息 uid:%d'%(int(uid)))
        return item
