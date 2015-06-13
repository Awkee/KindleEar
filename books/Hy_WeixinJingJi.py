#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return JingJiTouZiNews

class JingJiTouZiNews(WeixinBook):
    title                 = u'经济投资与电影'
    description           = u'了解经济、投资理财和电影相关资讯'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 7
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'中国经济网', 'http://weixin.sogou.com/gzh?openid=oIWsFt0B7LsVbUCMpgksNY8tqIno'),
            (u'投资潮','http://weixin.sogou.com/gzh?openid=oIWsFt8I2-vCYv8q0_3Kv9qDeqjg'),
            (u'投资理财','http://weixin.sogou.com/gzh?openid=oIWsFt0UVwWV9Sj3w_Sy8Idmx_qc'),
            (u'读心术','http://weixin.sogou.com/gzh?openid=oIWsFt-Na2DIcalk0pZ2eqW4bE1Q'),
            (u'电影天堂','http://weixin.sogou.com/gzh?openid=oIWsFtwSROy4gNoVFExXhAJXXoiU'),
            (u'电影工厂','http://weixin.sogou.com/gzh?openid=oIWsFt3Pmplza8bDhTkgr89hpzVU'),
            (u'只图好看','http://weixin.sogou.com/gzh?openid=oIWsFtyhD9jTNan9kV3EDmlrDwag'),
            (u'亿万富翁俱乐部','http://weixin.sogou.com/gzh?openid=oIWsFt9pfd_w39cfu-q92GkRhb8g')
            ]
