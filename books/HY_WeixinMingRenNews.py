#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinMingRenNews

class WeixinMingRenNews(WeixinBook):
    title                 = u'微信订阅:名人微信公众号'
    description           = u'搜集名人微信公众号发布信息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 15
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'李开复','http://weixin.sogou.com/gzh?openid=oIWsFt41pjHljjrbR9wk0L6dWmms'),
            (u'丹独约见','http://weixin.sogou.com/gzh?openid=oIWsFt3WNbLUvKout1f_qeCVyizQ'),
            (u'刀哥日志','http://weixin.sogou.com/gzh?openid=oIWsFt3NtuGk3uSE8evYg1oepiRE'),
            (u'手赚达人','http://weixin.sogou.com/gzh?openid=oIWsFt22bDadhuTiO9zoObhBkgBU')
            ]
