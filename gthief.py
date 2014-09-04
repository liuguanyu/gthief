#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 抓取小游戏
from Fetcher import *
from Parser import *
from Modifier import *

def deal_with_img(img_list , base_url) :
    imgf = ImageFetcher()

    img_local = []
    for ori , absolute , content in img_list:
        img = imgf.fetch(absolute)

        img_local.append({
            "ori" : ori ,
            "absolute" : absolute ,
            "content"  : img           
        })

    return img_local  

def deal_with_script(script_list , base_url):
    scriptf = ScriptFetcher()

    ssm = SixeScriptModifier()

    script_modified = []
    for ori , absolute , content in script_list:
        script = scriptf.fetch(absolute , content)
        script = ssm.modify(script , base_url)    

        script_modified.append({
            "ori" : ori ,
            "absolute" : absolute ,
            "content"  : script           
        })        
        
    return script_modified    

def main() :
    url = "http://www.6egame.com/game/106/"
    cf = CommonFetcher()
    html = cf.fetch(url)

    rp = ResourcesParser(url)
    resources = rp.parse(html)

    resources["img"] = deal_with_img(resources["img"] , url) 
    resources["script"] = deal_with_script(resources["script"] , url) 
    
    #print resources  

if __name__ == "__main__" : 
   main()  