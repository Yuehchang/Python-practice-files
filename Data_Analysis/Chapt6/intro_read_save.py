#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:43:13 2017

@author: changyueh
"""

#讀寫文本格式的數據，page162表6-1, page167/168表6-2(read_csv參數的介紹)
"""
read_csv
read_table
此兩款是最常用的
"""
import pandas as pd
import numpy as np

df = pd.read_csv('ex1.csv') # df = pd.read_table('ex1.csv', sep=',')兩者一樣

df1 = pd.read_csv('ex2.csv', header=None)
df1 #pandas默任其列名

df2 = pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
df2 #也可以自己設定columns名

names=['a', 'b', 'c', 'd', 'message']
pd.read_csv('ex2.csv', names=names, index_col='message') #可以將message那columns設定成index

pd.read_csv('ex3.csv', index_col=['key1', 'key2']) #利用list來製造多個層次化索引

list(open('ex3.txt'))
pd.read_table('ex3.txt', sep='\s+') #正規表達式在*精通python_page172/174，pd自動把第一row判別為Header

pd.read_csv('ex4.csv', skiprows=[0, 2])

pd.read_csv('ex5.csv') #自動把缺值補成NAN
pd.read_csv('ex5.csv', na_values=['NULL'])

##逐塊讀取文件
result =  pd.read_csv('ex6.csv', nrows=5)
result #只讀取文件nrows指定的rows

chunker = pd.read_csv('ex6.csv', chunksize=100)
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)

##將數據寫出到文本格式
df3 = pd.read_csv('ex5.csv')
df3
df3.to_csv('ex5_out.csv')
import sys
df3.to_csv(sys.stdout, sep='|') #利用sys.stdout來展現打印結果部真的輸出，sep改變分隔模式
df3.to_csv(sys.stdout, na_rep='NULL') #na_rep改變NAN值得輸出結果
df3.to_csv(sys.stdout, index=False, header=False) #index跟header都可以取消
df3.to_csv(sys.stdout, index=False, columns=['a', 'c', 'd']) #可以指定columns的輸出順序

dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('tseries.csv') #Series也可以使用to_csv

pd.Series.from_csv('tseries.csv', parse_dates=True) #可以用read_csv，但是from_csv更快速

##手工處理分隔符格式，page172有更多可查看（例如定義新格式）
import csv
f = open('ex7.csv')
reader = csv.reader(f)
reader #不是variable
for line in reader:
    print (line)

lines = list(csv.reader(open('ex7.csv'))) #把上述的結果變成一行
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))} #轉變成dict就可以變成DF

#JSON數據
obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": Scott", "age": 25, "pet": "Zuko"},
                {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""
import json
result = json.loads(obj) #Error，先保留之後處理

#XML and HTML
from lxml.html import parse
from urllib.request import urlopen

parsed = parse(urlopen('https://finance.yahoo.com/quote/AAPL/options?ltr=1'))
doc = parsed.getroot()
links = doc.findall('.//a') #查詢的一種手段
links[15:20]

lnk = links[28]
lnk
lnk.get('href')
lnk.text_content() #其中一條URL，text_cotent顯示文本

urls = [lnk.get('href') for lnk in doc.findall('.//a')] #取得所有URL
urls[-10:]

tables = doc.findall('.//table')
calls = tables[1] 
puts = tables[2] #還要學習如和從網站找出來，目前看應該是1跟2
rows = calls.findall('.//tr')
def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]
_unpack(rows[0], kind='th')
_unpack(rows[1], kind='td')

from pandas.io.parsers import TextParser
def parse_options_data(table):
    rows = table.findall('.//tr') #
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()
call_data = parse_options_data(calls)
put_data = parse_options_data(puts) #正式把資料讀取成DF

##利用lxml.objectify解析XML
"""
網站的數據需要key才能下載，就不另行下載page177-179是需要再次看的，練習XML的操作
"""

#二進位數據格式
df4 = pd.read_csv('ex1.csv')
df4.to_pickle('frame_pickle')
df4.read_pickle('frame_pickle') #沒辦法跑

##使用HDF5格式
store = pd.HDFStore('mydata.h5')
store['obj1'] = df
store['obj1_col'] = df['a']
store
store['obj1'] #可以通過像字典一樣的方式進行獲取

#使用HTML和WebAPI
import requests
url = 'http://search.twitter.com/search.json?q=python%20pandas' #API掛掉了
resp = requests.get(url)
resp
import json
data = json.loads(resp.text)
data.keys() #正常應該回傳一段類似字典的字串，其中裡面又包含所需的資訊在result中
tweet_fields = ['created_at', 'from_user', 'id', 'text'] #找出感興趣的columns
tweets = DataFrame(data['result'], columns=tweet_fields) #製作成DF可以看到什麼時候生成並且是誰做的等資訊

#使用數據庫
run ex8_sqlite3.py

cursor = con.execute('SELECT * FROM test')
rows = cursor.fetchall()
rows
cursor.description
pd.DataFrame(rows, columns=zip(*cursor.description)[0]) #zip不能subscription，標columns
#import pandas.io.sql as sql
pd.read_sql_query('select * from test', con)
pd.read_sql('select * from test', con)

#存取MongoDB中的數據，再繼續看