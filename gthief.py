#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 抓取小游戏
from Fetcher import *
from Parser import *

def deal_with_img(img_list) :
    imgf = ImageFetcher()

    img_local = []
    for absolute , ori in img_list:
        img = imgf.fetch(absolute)

        img_local.append({
            "ori" : ori ,
            "absolute" : img            
        })

    return img_local  

def main() :
    url = "http://www.6egame.com/game/106/"
    cf = CommonFetcher()
    html = cf.fetch(url)

    rp = ResourcesParser(url)
    resources = rp.parse(html)

    resources["img"] = deal_with_img(resources["img"]) 
    
    print resources  

if __name__ == "__main__" : 
   main()  