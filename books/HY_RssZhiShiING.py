#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return RSSZhiShiING

class RSSZhiShiING(BaseFeedBook):
    title                 = u'知食ING'
    description           = u'每日限量精选美食推荐'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_ebrun.gif"
    coverfile             = "cv_ebrun.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'知食ING', 'https://diy-devz.rhcloud.com/gzh?openid=oIWsFtxQZDXHaYVoxxJ1rK4NJKCg')
            ]

    def fetcharticle(self, url, opener, decoder):
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        