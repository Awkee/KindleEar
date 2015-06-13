#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return YiYanRSSNews

class YiYanRSSNews(BaseFeedBook):
    title                 = u'译言RSS订阅资源'
    description           = u'译言口号：发现、阅读中文之外的互联网精华，创始人：三名在美国硅谷工作的中国工程师'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_yiyan.gif"
    coverfile             = "cv_yiyan.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'最新精选', 'http://feed.yeeyan.org/select'),
            (u'最新译文','http://feed.yeeyan.org/latest'),
            (u'商业频道','http://feed.yeeyan.org/business'),
            (u'科技频道','http://feed.yeeyan.org/tech'),
            (u'文化频道','http://feed.yeeyan.org/culture'),
            (u'体坛频道','http://feed.yeeyan.org/sport'),
            (u'健康频道','http://feed.yeeyan.org/health'),
            (u'自然频道','http://feed.yeeyan.org/nature'),
            (u'生活频道','http://feed.yeeyan.org/life'),
            (u'社会频道','http://feed.yeeyan.org/society')
            ]

    def fetcharticle(self, url, opener, decoder):
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        