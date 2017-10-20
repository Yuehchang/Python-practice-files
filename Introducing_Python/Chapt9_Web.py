#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 12:38:31 2017

@author: changyueh
"""

#web 
"""
1. HTTP (Hypertext Transfer Protocol)
2. HTML (Hypertext Markup Language)
3. URL (Uniform Resource Locatar)
"""

#telnet來測試page 237
#可以使用shell取得一些資訊

#Python的表準Web程式庫
"""
套件1. http
* client 負責用戶端的工作
* server 負責幫助你編寫Python web伺服器
* cookies & cookiejar 負責管理cookie，與他在多次造訪網站之間的存儲資料

套件2. urllib
* request 負責處理用戶端請求
* response 負責處理伺服器回應
* parse 負責拆解URL的各個部分
"""

import urllib.request as ur
url = 'http://www.iheartquotes.com/api/v1/random'
conn = ur.urlopen(url)
print(conn)

#轉去看Web Crawling