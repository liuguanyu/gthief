#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 抓取小游戏工厂方法，外界直接和这个类打交道

from HTMLParser import HTMLParser
from urlparse import urljoin

class ResourcesParser (HTMLParser): 
    use_inner_data = False

    note_tag = ("script" , "img")

    resources = {}

    def __init__(self , base_url):
        HTMLParser.__init__(self)
        self.base_url = base_url

    def handle_data(self , data):
        self.use_inner_data = False    

    def handle_starttag (self , tag , attrs):
         if tag in self.note_tag:
            script_has_src = False

            if len(attrs) == 0: 
                if tag in ("script"):
                    self.use_inner_data = True

                return 

            for (variable, value)  in attrs:
                if variable == "src":
                    if tag == "script" :
                        script_has_src = True 
                     
                    self.resources.setdefault(tag , [])
                    self.resources[tag].append([value , urljoin(self.base_url , value)])     

            if script_has_src == False and tag == "script" :
                self.use_inner_data = True

    def parse (self , html_str):
        self.feed(html_str)
        self.close()

        return self.resources

if __name__ == "__main__" :
    foo = ResourcesParser("http://me.com")
    print foo.fetch(url)               