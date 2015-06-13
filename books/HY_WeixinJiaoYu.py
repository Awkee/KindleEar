#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinJiaoYuNews

class WeixinJiaoYuNews(WeixinBook):
    title                 = u'微信订阅:教育类'
    description           = u'了解与教育相关最新推送消息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 15
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'友题','http://weixin.sogou.com/gzh?openid=oIWsFtw9JJv0Y09FVRzfkOrZMli8')
            ]
