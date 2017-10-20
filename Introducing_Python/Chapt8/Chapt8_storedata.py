#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 08:24:08 2017

@author: changyueh
"""

"""
開啟檔案
fileobj = open(filename, mode)

mode第一個字母有是操作
1. r = read / 2. w = write / 3. x = write if file doesn't exist
4. a = append

mode第二個字母是檔案的類型
1. t = text / 2. b = byte

"""
#write()來編寫檔案
poem = '''There was a young lady named Bright, 
Whose speed was far faster than light;
She started one day
In a relative way, 
And returned on the previous night.'''

len(poem)

fout = open('relativity', 'wt')
fout.write(poem) #write函數會顯示被寫入的byte數量
fout.close()
          
#fout = open('relativity', 'wt')
#print(poem, file = fout)
#fout.close() #same as we metioned above 

#print跟write不同，print會加入空格與換行符號
#print(poem, file = fout, sep = '', end = '') #這樣即可解決加入sep & end

#如果字源過大，可以分段加
fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close()

#避免複寫
fout = open('ralativity', 'xt')

try:
    fout = open('relativity', 'xt')
    fout.write('stomp, stomp, stomp')
except FileExistsError:
    print('Error')

#用read()、readline()、readlines()來讀取文字檔
fin = open('relativity', 'rt')
poem1 = fin.read()
fin.close()
len(poem1)

######### practice read
poem2 = ''
chunk = 100
fin1 = open('relativity', 'rt')

while True:
    fragment = fin1.read(chunk)
    if not fragment: #這邊邏輯還是不太清楚
        break 
    poem2 += fragment 

fin1.close()
len(poem2)

######### practice readline
poem3 = ''
fin2 = open('relativity', 'rt')
while True:
    line = fin2.readline()
    if not line:
        break
    poem3 += line
fin.close()
len(poem3)

######### practice 迭代
poem4 = ''
fin3 = open('relativity', 'rt')
for fin in fin3:
    poem4 += fin
fin3.close()
len(poem4)

########## practice readlines
fin4 = open('relativity', 'rt')
lines = fin4.readlines()
fin4.close()
print(len(lines), 'lines read')

#write()寫入二進位檔案
bdata = bytes(range(0, 256))
len(bdata)

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

##########分段寫入
fout = open('bfile', 'wb')
size = len(bdata) #忘記加這個
start = 0
offset = 100
while True:
    if start > size:
        break
    fout.write(bdata[start : start + offset])
    start += offset 
fout.close()

#用read()來讀取二進位檔案
fin5 = open('bfile', 'rb')
bdata = fin5.read()
len(bdata)
fin5.close()

#用with來自動關閉檔案 page193

#用seek()來更改位置
fin6 = open('bfile', 'rb')
fin6.tell() #回傳檔案的開頭算起，目前的位移值
fin6.seek(225)
bdata1 = fin6.read()
len(bdata1)
bdata1[0] #應該是1才對，我的出現31

#文字檔結構 - CVS、XML、JSON、YAML
# 輸入進csv
import csv
villains = [
        ['Doctor', 'No'],
        ['Rosa', 'Klebb'],
        ['Mister', 'Big'],
        ['Auric', 'Goldfinger'],
        ['Ernst', 'Blofeld']
        ] #list 

with open('villains', 'wt') as fout: #a context manager(自動會關閉，不用寫close)
    csvout = csv.writer(fout)
    csvout.writerows(villains)
    
# 讀回python
with open('villains', 'rt') as fin:
    cin = csv.reader(fin)
    villains1 = [row for row in cin]
print(villains1)

#資料可以讀成一串字典
with open('villains', 'rt') as fin1:
    cin1 = csv.DictReader(fin1, fieldnames=['first', 'last']) #keyN = first, valueN = last 
    villains2 = [row for row in cin1]

print(villains2)

#重新用DictWriter寫入csv
with open('villains1', 'wt') as fout1: #villains1就有first, last的表頭
    cout = csv.DictWriter(fout1, ['first', 'last'])
    cout.writeheader() #要有表頭
    cout.writerows(villains2) #寫進villains2是字典的不是list的
    
with open('villains1', 'rt') as fin2:
    cin2 = csv.DictReader(fin2) #這邊沒有fieldnames因為預設第一行就是key＆value
    villains3 = [row for row in cin2] #villains3要和villains2一樣

#XML page198
import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml') #讀不進去
root = tree.getroot()
root.tag

#JSON JavaScript Object Notation
menu = \
{
"breakfast": {
        "hours": "7-11",
        "items": {
                "breakfast burritos" : "$6.00",
                "pancakes": "$4.00"
                }
        },
"lunch": {
        "hours": "11-3",
        "items": {
                "hamburger": "$5.00"
                }
        },
"dinner":{
        "hours": "3-10",
        "items": {
                "spaghetti": "$8.00"
                }
        }        
}
        
import json
menu_json = json.dumps(menu) #dumps編碼成JSON字串

menu2 = json.loads(menu_json) #loads轉回pyhton結構

##JSON並未定義日期與時間的類型，因此需要把datatime轉乘JSON瞭解的東西
##practice
import datetime
now = datetime.datetime.utcnow()

from time import mktime

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime): #檢查obj的類型
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

json.dumps(now, cls=DTEncoder) #再看一次

#YAML 還沒操作，回頭再看

#設定檔 還沒操作，回頭再看
#用pickle來序列化 還沒操作，回頭再看

#結構化的二進位檔案 - 試算表、HDF5

#關聯資料庫 - SQL、DB-API

#SQLite
import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor() #建立一個cursor物件來處理查詢指令
curs.execute('''CREATE TABLE zoo
(critter VARCHAR(20) PRIMARY KEY,
count INT,
damages FLOAT)''') #建立schema #已經有了第二次就不建造table

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

#佔位符，另一種安全的資料插入方式
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))

#全部取出
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

#排序
curs.execute('SELECT * FROM zoo ORDER BY count')
curs.fetchall()

curs.execute('SELECT * FROM zoo ORDER BY count DESC')
curs.fetchall()

#挑花費最多
curs.execute('''SELECT * FROM zoo WHERE
             damages = (SELECT MAX(damages) FROM zoo)''')
curs.fetchall()

curs.close()
conn.close()

#PostgreSQL => import pyscopg2已經有在lib

#SQLAlchemy => 已經在lib李了
'''
一開始要處理需要輸入下列字串提供SQLAlchemy與之前資料驅動合作

dialect + driver :// user : password @ host : port / dbname

1. 資料庫類型
2. 特定資料驅動程式
3. / 4. 資料庫驗證字串
5. / 6. 資料庫伺服器位置 (當不是標準設定時，才需要port)
7. 一開始連接的伺服器資料庫

表8.5 列出各方言與伺服器 page216
'''
#practice 最底層 引擎層
import sqlalchemy as sa #別名登入
conn = sa.create_engine('sqlite://') #省略中間所有和dbname，系統直接預設
conn.execute('''Create TABLE zoo
             (critter VARCHAR(20) PRIMARY KEY,
             count INT,
             damages FLOAT)''') #運行時回傳ResultProxy的物件

ins = 'INSERT INTO zoo (critter, count, damages) VALUEs (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)

#查詢
rows = conn.execute('SELECT * FROM zoo')
print(rows) #不是普通的串列，是ResultProxy，因此沒有辦法直接打印
results = [row for row in rows]
print(results) #每次打印都需要跟著rows(指令)一起跑，不然會回傳空的list or values
 
#practice 中間層 SQL Expression Language
import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
meta = sa.MetaData() #different than the practice above 
zoo = sa.Table('zoo', meta,
               sa.Column('critter', sa.String, primary_key = True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float)
               )
meta.create_all(conn)

conn.execute(zoo.insert(('duck', 10, 0.0)))
conn.execute(zoo.insert(('bear', 2, 1000.0)))
conn.execute(zoo.insert(('weasel', 1, 2000.0))) 

results1 = conn.execute(zoo.select())             
rows1 = results1.fetchall()
print(rows1)

#pratice 最頂層ORM
import sqlalchemy as sa 
from sqlalchemy.ext.declarative import declarative_base #different from SQL Expression Language

conn = sa.create_engine('sqlite:///zoo.db') #連結

Base = declarative_base() #進入ORM並建立Zoo類別，建立資料表欄位
class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key = True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

Base.metadata.create_all(conn)#會建立資料庫與資料表
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0) #建立Python物件來插入資料

from sqlalchemy.orm import sessionmaker #利用ORM前往SQL
Session = sessionmaker(bind=conn)
session = Session()

session.add(first) #add one
session.add_all([second, third]) #add all

session.commit()

"""
完整ORM教程 http://bit.ly/obj-rel-tutorial
"""    
     
#NoSQL 資料存放區
#dbm家族 如同字典一樣
import dbm
db = dbm.open('definitions', 'c') #r代表read，w代表write，c代表read&write 
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'

db.close()#先關閉在打開檢查，是否真的寫入
db = dbm.open('definitions', 'r')
db['mustard']
db['salsa'] = 'red'#只read無法寫入
db.close                     
                       
#Memcached(http://memcached.org/)
#Redis(http://redis.io) page 223
"""
剩餘的Chapt8都在說如何連接Redis資料結構伺服器，
並在python中使用其中的資料（必要的指令教學）
"""


                       
                       
                       
                       