#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 分析小游戏基本的资源

from HTMLParser import HTMLParser
from urlparse import urljoin

class ResourcesParser (HTMLParser): 
    use_inner_data = False

    note_tag = ("script" , "img" , "style" , "link")
    block_tag = ("script" , "style")

    resources = {"img" : [] , "script" : [] , "style" : [] , "link" : []}

    def __init__(self , base_url):
        HTMLParser.__init__(self)
        self.base_url = base_url

    def handle_data(self , data):
        if self.use_inner_data == True :
            self.data = data

    def handle_starttag (self , tag , attrs):
         if tag in self.note_tag:
            script_has_src = False

            if len(attrs) == 0: 
                if tag in self.block_tag:
                    self.use_inner_data = True

                return 

            for (variable, value)  in attrs:
                if variable == "src":
                    if tag == "script" :
                        script_has_src = True 
                     
                    self.resources[tag].append([value , urljoin(self.base_url , value) , ''])   

                if  variable == "href" and tag == "link" :
                    self.resources[tag].append([value , urljoin(self.base_url , value) , ''])  


            if script_has_src == False and tag in self.block_tag :
                self.use_inner_data = True

    def handle_endtag(self , tag):
        if tag in ("script") and self.use_inner_data == True:     
            self.resources[tag].append(['' , '' , self.data])
            self.data = ""
            self.use_inner_data = False

    def parse (self , html_str):
        self.feed(html_str)
        self.close()

        return self.resources

if __name__ == "__main__" :
    foo = ResourcesParser("http://me.com")
    print foo.fetch(url)               