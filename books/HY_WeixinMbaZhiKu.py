#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinMbaZhiKuNews

class WeixinMbaZhiKuNews(WeixinBook):
    title                 = u'微信订阅:MBA智库'
    description           = u'了解MBA智库推送的消息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 7
    deliver_times = [8,20]
    feeds = [
            (u'MBA智库','http://weixin.sogou.com/gzh?openid=oIWsFt5P_R_eX-7b2Ck-kCPWvsZ8'),
            (u'MBA智库资讯','http://weixin.sogou.com/gzh?openid=oIWsFt3zbfwy6BMBrMszxQRuyKZw'),
            (u'MBA智库百科','http://weixin.sogou.com/gzh?openid=oIWsFtzBJvBgS1VqhhLq85iyqp1k'),
            (u'MBA智库商学苑','http://weixin.sogou.com/gzh?openid=oIWsFt_h5jNOO4-8H88VaBl35j9U')
            ]
