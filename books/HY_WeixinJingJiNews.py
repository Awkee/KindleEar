#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinJingJiNews

class WeixinJingJiNews(WeixinBook):
    title                 = u'微信订阅:经济类'
    description           = u'了解每日经济新闻最新消息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 15
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'中国经济网','http://weixin.sogou.com/gzh?openid=oIWsFt0B7LsVbUCMpgksNY8tqIno'),
            (u'投资潮','http://weixin.sogou.com/gzh?openid=oIWsFt8I2-vCYv8q0_3Kv9qDeqjg'),
            (u'投资理财','http://weixin.sogou.com/gzh?openid=oIWsFt0UVwWV9Sj3w_Sy8Idmx_qc'),
            (u'凤凰财经','http://weixin.sogou.com/gzh?openid=oIWsFt4JERI6aVU7J1rs8Dt3KXGI')
            ]
