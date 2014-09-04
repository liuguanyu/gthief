#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- author:liuguanyu -*-
# 修改6egame小游戏资源文字及资源依赖

from commonscriptmodifier import *
from urlparse import urljoin
from Fetcher.imagefetcher import *
import re

HOME_URL = "http://shanku.hao.360.cn/mobile"
THIEF_NAME = "闪酷游戏"
OWNER_NAME = "6e游戏"

CURRENT_URL = "location.href"

class SixeScriptModifier (CommonScriptModifier):
    text = ""

    # 替换入口    
    def modify(self , script , base_url):
        self.text = script
        self.base_url = base_url

        self.__delete_detector().__delete_rotate()
        self.__delete_their_config().__delete_weixin_surplus()

        self.__modify_script_image().__modify_weixin_config()

        #print self.text
        return self.text 

    # 删除横屏检测函数        
    def __delete_rotate (self):
        repl = 'var RESOURCE_IMG_PATH.*?window\.addEventListener\("scroll", r\)'
        self.text = re.sub(repl , "" , self.text , 0 , re.IGNORECASE | re.DOTALL | re.MULTILINE)  

        return self

    # 删除游戏主的配置  
    def __delete_their_config(self):
        m = re.search("_config\['isSite'\]" , self.text , re.IGNORECASE | re.DOTALL)

        if m :
            self.text = ""

        return self    

    # 删除游戏主的微信干扰信息 
    def __delete_weixin_surplus(self) :
        m = re.search("weiapp.552200.com" , self.text , re.IGNORECASE | re.DOTALL)

        if m :
            self.text = ""

        return self     

    # 替换游戏主的微信信息
    def __modify_weixin_config(self):

        def __modify_home_url(mch):
            return mch.group(0).replace(mch.group(1) , HOME_URL)

        repl = 'var mebtnopenurl = [\'"](.*?)[\'"]'  
        self.text = re.sub(repl ,  __modify_home_url , self.text , re.IGNORECASE | re.DOTALL); 

        self.text = self.text.replace(OWNER_NAME , THIEF_NAME)
        '''
        repl = 'dataForWeixin\s*?=\s*?{.*?\"url\"\s*?:\s*?([\'"].*?[\'"]).*?}'

        def __modify_current_url(mch):
            print mch.group(0)
            return mch.group(0).replace(mch.group(1) , CURRENT_URL)

        self.text = re.sub(repl , __modify_current_url , self.text , re.IGNORECASE | re.DOTALL | re.MULTILINE)     

        #print self.text  
        '''  
        return self   

    # 替换游戏主在脚本里的图片  
    def __modify_script_image(self):
        repl = '[\'"](\/vapp.*?)[\'"]'
        imgf = ImageFetcher()

        def __fetch_image_and_replace(mch):
            image_url = mch.group(1)
            absolute_url = urljoin(self.base_url , image_url)

            new_url = imgf.fetch(absolute_url)    
            return '"' + new_url + '"'

        self.text = re.sub(repl , __fetch_image_and_replace , self.text , re.IGNORECASE | re.DOTALL)

        return self                      

    # 删除游戏主检测手机的代码        
    def __delete_detector(self):
        m = re.search("isShouji" , self.text , re.IGNORECASE | re.DOTALL)

        if m :
            self.text = ""

        return self  