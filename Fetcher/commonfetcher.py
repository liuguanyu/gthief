#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 抓取小游戏工厂方法，外界直接和这个类打交道

import urllib2

class CommonFetcher (object) :
    headers = ('User-Agent','Mozilla/5.0 (Linux; U; Android 4.2.2; zh-CN; GT-I9500 Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/533')

    def __init__(self) :
        pass

    def fetch (self , url):
        opener = urllib2.build_opener()
        opener.addheaders = [self.headers]
        return opener.open(url).read() 

if __name__ == "__main__" :
    foo = CommonFetcher()
    print foo.fetch(url)               