#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 抓取小游戏图片方法

from commonfetcher import *
from Util import *

class ImageFetcher(CommonFetcher) :
    pbc = PicBedClient()

    def fetch (self , url):
        data = super(ImageFetcher , self).fetch(url)
        #print "正在上传到图床"
        new_url = self.pbc.save(data)
        #print "新url为" + new_url        
        return new_url 

if __name__ == "__main__" :
    foo = CommonFetcher()
    print foo.fetch(url)               