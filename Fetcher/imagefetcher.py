#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 抓取小游戏工厂方法，外界直接和这个类打交道

from commonfetcher import *
import base64
from Util import *

class ImageFetcher(CommonFetcher) :
    pbc = PicBedClient()

    def fetch (self , url):
        data = super(ImageFetcher , self).fetch(url)
        return self.pbc.save(data) 

if __name__ == "__main__" :
    foo = CommonFetcher()
    print foo.fetch(url)               