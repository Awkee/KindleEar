#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return FTChinese

class FTChinese(BaseFeedBook):
    title                 = u'FT中文网'
    description           = u'英国《金融时报》集团旗下唯一的中文商业财经网站。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_ftchinese.gif"
    coverfile             = "cv_ftchinese.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'每日更新', 'http://www.ftchinese.com/rss/feed'),
            (u'今日焦点','http://www.ftchinese.com/rss/news'),
            (u'十大热门文章','http://www.ftchinese.com/rss/hotstoryby7day'),
            (u'每日英语','http://www.ftchinese.com/rss/diglossia'),
            (u'第一时间解读','http://www.ftchinese.com/rss/column/007000005'),
            (u'远观中国','http://www.ftchinese.com/rss/column/007000004'),
            (u'中国纪事','http://www.ftchinese.com/rss/column/007000007'),
            (u'朝九晚五','http://www.ftchinese.com/rss/column/007000002'),
            (u'生活时尚','http://www.ftchinese.com/rss/lifestyle'),
            (u'读者有话说','http://www.ftchinese.com/rss/letter'),
            (u'马丁 沃尔夫','http://www.ftchinese.com/rss/column/007000012')
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
        