#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 抓取小游戏脚本方法

from commonfetcher import *
from Util import *

class ScriptFetcher(CommonFetcher) :
    pbc = PicBedClient()

    def fetch (self , url , content):
        data = content if url == "" else super(ScriptFetcher , self).fetch(url)
        return data

if __name__ == "__main__" :
    foo = CommonFetcher()
    print foo.fetch(url)        