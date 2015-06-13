#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinFilmNews

class WeixinFilmNews(WeixinBook):
    title                 = u'微信订阅:影视类'
    description           = u'了解每日影视资讯最新消息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 15
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'电影天堂','http://weixin.sogou.com/gzh?openid=oIWsFtwSROy4gNoVFExXhAJXXoiU'),
            (u'电影工厂','http://weixin.sogou.com/gzh?openid=oIWsFt3Pmplza8bDhTkgr89hpzVU'),
            (u'只图好看','http://weixin.sogou.com/gzh?openid=oIWsFtyhD9jTNan9kV3EDmlrDwag'),
            (u'亿万富翁俱乐部','http://weixin.sogou.com/gzh?openid=oIWsFt9pfd_w39cfu-q92GkRhb8g')
            ]
