#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return Weixin_sjzh1111

class Weixin_sjzh1111(WeixinBook):
    title                 = u'微信订阅:商界智慧'
    description           = u'了解商界智慧最新推送消息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 15
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'商界智慧','http://weixin.sogou.com/gzh?openid=oIWsFtx5ME8z2icY5YQ6GjaAXmXs')
            ]
