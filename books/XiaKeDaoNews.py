#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return XiaKeDaoNews

class XiaKeDaoNews(WeixinBook):
    title                 = u'微信公众号：政治新闻'
    description           = u'只有小道消息才能拯救中国互联网'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 7
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'创业', 'http://weixin.sogou.com/gzh?openid=oIWsFt8OYQYAAoIYg5WRTNq78KDA'),
            (u'侠客岛', 'http://weixin.sogou.com/gzh?openid=oIWsFt5EljIYAz8W3JBwW8bhN700'),
            (u'政治风云', 'http://weixin.sogou.com/gzh?openid=oIWsFt2gxn1udFjyBaPT5WucNueE'),
            (u'野史秘闻', 'http://weixin.sogou.com/gzh?openid=oIWsFt7LuTaYItJI8OAjfQNmSFXk'),
            (u'中国国家地理', 'http://weixin.sogou.com/gzh?openid=oIWsFt1A6Sh5-NrFDwq0l-q1Hvzs'),
            (u'历史真相解密大全', 'http://weixin.sogou.com/gzh?openid=oIWsFty8860rrTe2msNlZ1GQEKRA')
            ]
