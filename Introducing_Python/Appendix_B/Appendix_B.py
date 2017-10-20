#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 14:04:02 2017

@author: changyueh
"""

#Microsoft Office套件
"""
1. docx(pypi.python.org/pypi/docx)
* 可建立、讀取、寫入Word2007.docx檔案

2. python-excel(www.python-excel.org/)
* 有xlrd、xlwt、xlutils模組可用
* 也可以用csv模組處理

3. oletools(bit.ly/oletools)
* 可以攝取office格式的資料

4. OpenOffice(openoffice.org) page380 

還有很多可以用，查看page380 - 381
"""

#practice page383
#create a csv
list = [
        ['animal', 'bites', 'stitches', 'hush'],
        ['bear', '1', '35', '300'],
        ['marmoset', '1', '2', '250'],
        ['bear', '2', '42', '500'],
        ['elk', '1', '30', '100'],
        ['weasel', '4', '7', '50'],
        ['duck', '2', '0', '10'],
        ]

import csv 
with open('zoo.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(list) #input list's data to zoo.csv
    
#計算Counter() => 在zoo_counts.py
#其他資料資源 p385

#地圖 更多說明在p387
