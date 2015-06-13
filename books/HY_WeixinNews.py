#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinNews

class WeixinNews(WeixinBook):
    title                 = u'微信订阅:新闻类'
    description           = u'了解每日新闻最新消息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 15
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'人民邮电报','http://weixin.sogou.com/gzh?openid=oIWsFtyd30myszNFV0VNiF_QCuXE'),
            (u'人民日报','http://weixin.sogou.com/gzh?openid=oIWsFt8_jYUmdw1PQgNVhH9vOEvI'),
            (u'央视新闻','http://weixin.sogou.com/gzh?openid=oIWsFt_IC706OXjJP2sn_T5MxVfs'),
            (u'央视新闻周刊-岩松说','http://weixin.sogou.com/gzh?openid=oIWsFt4qR8yMywz7I3x1qAj3_7bU')
            ]
