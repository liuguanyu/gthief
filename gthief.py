#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 抓取小游戏
from Fetcher import *
from Parser import *

def main() :
    url = "http://www.6egame.com/game/106/"
    cf = CommonFetcher()
    html = cf.fetch(url)

    rp = ResourcesParser(url)
    resources = rp.parse(html)

    imgf = ImageFetcher()

    for absolute , ori in resources["img"] :
        img = imgf.fetch(absolute)
        print absolute
        print "==="
        print img
        print "\n"

if __name__ == "__main__" : 
   main()  