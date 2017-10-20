#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 08:51:12 2017

@author: changyueh
"""

#來自bit.ly的1.usa.gov資料
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()

import json
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
#data_json = json.dumps(path)
records = [json.loads(line) for line in open(path)] #開不了，還需要找出問題 => copypaste不能打開，但是直接另存新檔成txt就可以！

records[0]#轉變成字典
records[0]['tz']           
           
#用Python對時區進行計數
time_zone = [rec['tz'] for rec in records] #並不是所有records都有'tz'
time_zone = [rec['tz'] for rec in records if 'tz' in rec]

time_zone[:10] #前十個

#practice1
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1 
    return counts    

tz_counts = get_counts(time_zone)
tz_counts       

#makeup p1
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x not in counts:
            counts[x] = 1 #只會記錄一次
        #else:
            #counts[x] = 1 
    return counts    

tz_count = get_counts(time_zone)
tz_count       

#practice2
from collections import defaultdict

def get_counts1(sequence):
    counts = defualtdict(int) 
    for x in sequence:
        counts[x] += 1
    return counts

#practice3 top 10 
def top_counts(count_dict, n=10):
    value = [(count, tz) for tz, count in count_dict.items()]
    value.sort()
    return value[-n:]

top_counts(tz_counts) #sort字母

#simpler practice3
from collections import Counter
counts = Counter(time_zone)
counts.most_common(10)
    
##利用pandas進行計數！
from pandas import DataFrame, Series
import pandas as pd; import numpy as np
frame = DataFrame(records) #直接利用key值當作表頭    
        
frame['tz'][:10] #可以排列出前10個
tz_count1 = frame['tz'].value_counts()#DataFrame的一個方法
tz_count1[:10]       

#利用matpotlib繪圖
clean_tz = frame['tz'].fillna('Missing') #空值可以替換成Missing
clean_tz[clean_tz == ''] = 'Unknown'
tz_count2 = clean_tz.value_counts()
tz_count2[:10]

tz_count2[:10].plot(kind='barh', rot=0)    

##利用正則表達式找出匹配項目
#找出windows/非windows
nonan_frame = frame[frame.a.notnull()] #首先把a的欄位的nan去除
operating_system = np.where(nonan_frame['a'].str.contains('Windows'), 'Windows', 'Not Windows')

#利用新的區分來進行分類
#by_tz_os = nonan_frame.groupby(['tz', operating_system]) #不會顯示在variable
#agg_counts = by_tz_os.size().unstack.fillna(0) #by_tz_os是個公式，所以沒辦法fillna，所以還區要找出問題點，未解決！！
#agg_counts[:10]