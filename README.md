# bilibili
基于scrapy框架，抓取bilibili前十万用户的个人信息 https://space.bilibili.com/1#/


存储在mysql数据库中


信息包括：uid 用户名 性别 地区 粉丝数 关注量 出生年月 播放量 等级 经验 注册时间 称号



其中 粉丝数和关注量 直接通过个人主页抓取较繁琐，利用了api


由于bilibili封ip原因，起先利用免费代理抓取，后发现代理经常失效不稳定，决定间隔3秒抓取一次


数据不做商业用途，仅供学习，谢谢！
