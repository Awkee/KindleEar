#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinTeleNews

class WeixinTeleNews(WeixinBook):
    title                 = u'微信订阅:电信行业领域'
    description           = u'了解每日电信行业领域资讯最新消息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 15
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'亚联广州之家','http://weixin.sogou.com/gzh?openid=oIWsFtyUHXbKNZFv5JYUObIvztNM'),
            (u'厦门中兴软创计费产品线','http://weixin.sogou.com/gzh?openid=oIWsFt7uvBfPtPjkWVu6Rpa8D_gw'),
            (u'益阳移动直通车','http://weixin.sogou.com/gzh?openid=oIWsFt8by8YyyQ9LzqA_YLCHiMKo'),
            (u'华南区微管理平台','http://weixin.sogou.com/gzh?openid=oIWsFt8l3vNmpTjr6KVataTowLS0'),
            (u'亚联江西BOSS项目组','http://weixin.sogou.com/gzh?openid=oIWsFt9hvgghjk8mFSRtfkoEDyWE'),
            (u'武汉电信实业','http://weixin.sogou.com/gzh?openid=oIWsFt42c1Y21_YKMaxOzv54-puU'),
            (u'钟楼漫谈','http://weixin.sogou.com/gzh?openid=oIWsFt8af5JF6ML7bIkM8iKuRU9E'),
            (u'思特奇人','http://weixin.sogou.com/gzh?openid=oIWsFt1A_0fpvfKniBmDoAnPiQII'),
            (u'信运那些事','http://weixin.sogou.com/gzh?openid=oIWsFt6jYXlKVV_Ls7G6vybMuD3Q'),
            (u'博赛网络','http://weixin.sogou.com/gzh?openid=oIWsFt4b5ROREIIfE-cLXIR21d6o'),
            (u'怀化联通信息化服务中心','http://weixin.sogou.com/gzh?openid=oIWsFtzO_10gizfMLDuutYAOsL5k'),
            (u'火花无限崔强','http://weixin.sogou.com/gzh?openid=oIWsFt2gbIZNf3_K1KeO9q5zXJm4'),
            (u'手机圈','http://weixin.sogou.com/gzh?openid=oIWsFt5rohtuBCE_PlivBqX39Sdc'),
            (u'电信创新手机圈','http://weixin.sogou.com/gzh?openid=oIWsFt5BqNFY1mh9eQHIX4rG7jGk'),
            (u'上海杰尔讯','http://weixin.sogou.com/gzh?openid=oIWsFt3jA4g7ekR3DWYMv5Gm-Ejg'),
            (u'C114中国通信网','http://weixin.sogou.com/gzh?openid=oIWsFtyKr5X08p0Ras7atvCgODZ4')
            ]
