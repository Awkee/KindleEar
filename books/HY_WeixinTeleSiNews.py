#!/usr/bin/env python
# -*- coding:utf-8 -*-
from weixinbase import WeixinBook

def getBook():
    return WeixinTeleSiNews

class WeixinTeleSiNews(WeixinBook):
    title                 = u'微信订阅:电信第三方企业资讯'
    description           = u'了解每日电信行业服务集成商领域资讯最新消息'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 7
    deliver_days = ['Friday']
    deliver_times = [8,20]
    feeds = [
            (u'华为','http://weixin.sogou.com/gzh?openid=oIWsFt3NcOiNVknqnZevHA71Giyo'),
            (u'华为招聘','http://weixin.sogou.com/gzh?openid=oIWsFt0xlUlxoy7k2CI2cocroAy0'),
            (u'华为企业业务','http://weixin.sogou.com/gzh?openid=oIWsFt4XCt8ihPcly3fqTkCAQyBE'),
            (u'爱立信中国','http://weixin.sogou.com/gzh?openid=oIWsFt_GUEKCf-etYtFmoLiV4QJo'),
            (u'爱立信学院','http://weixin.sogou.com/gzh?openid=oIWsFt6VcC8eJcUefI7AIlMu67Y4'),
            (u'爱立信招聘','http://weixin.sogou.com/gzh?openid=oIWsFt7Z39Y-6GBpw22uFzdZF7u4'),
            (u'诺西综合代维','http://weixin.sogou.com/gzh?openid=oIWsFt2AKNQHrQIXvP8hRX8p8dFA'),
            (u'大唐电信','http://weixin.sogou.com/gzh?openid=oIWsFt31cE38F3fnmrCpZERv_vxk'),
            (u'你好亚信人','http://weixin.sogou.com/gzh?openid=oIWsFt_Gt5HhjKjwjdx4I59f3LSE'),
            (u'GBase数据库','http://weixin.sogou.com/gzh?openid=oIWsFtyqQqKUb4ieBg2tSSIkVVS8')
            ]
