#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinHeAndSheNews

class WeixinHeAndSheNews(WeixinBook):
    title                 = u'微信订阅:他和她'
    description           = u'八卦新闻'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 15
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'他','http://weixin.sogou.com/gzh?openid=oIWsFt-fGiQX-vDnlF6PPXeBXyiQ'),
            (u'她','http://weixin.sogou.com/gzh?openid=oIWsFt3epigoySBIczbEm2YE61pI')
            ]
