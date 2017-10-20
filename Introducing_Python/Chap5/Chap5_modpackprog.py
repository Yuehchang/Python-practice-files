#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:46:49 2017

@author: changyueh
"""
#指令列引數
import sys
print('Program arguments:', sys.argv)

#匯入模組
import report 
description = report.get_description()
print ("Today's weahter:", description)

#模組搜尋路徑 page 121

#套件 page 121 weather.py / sources => daily.py weekly.py

"""
實用的標準程式庫 page123
#模組文件http://docs.python.org/3/library
#教學課程http://bit.ly/library-tour
#Python Module of the Week http://bit.ly/py-motw
#The Python Standard Library by Example http://bit.ly/py-libex
"""

#用setdefault()/defaultdict()來處理遺漏的鍵 page 123
periodic_table = {'Hydrogen' : 1, 'Helium' : 2}
periodic_table.get('Oxgen') #返回值
carban = periodic_table.setdefault('Carban', 12) #鍵如果沒有，就使用新值
helium = periodic_table.setdefault('Helium', 987) #已存在的鍵，值不會因此改變

#default()很類似，當字典被建立，會為任何新鍵制定預設值，引數是參數
from collections import defaultdict
periodic_table = defaultdict(int) #int()為一個函數
periodic_table['Hydrogen'] = 1
periodic_table['Lead']  #沒有設值，就是0預設

#practice
from collections import defaultdict

def no_idea():
    return 'Huh?'
    
bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
bestiary['C'] # output => 因為沒有設立值，所以會直接是‘Huh?'

bestiary = defaultdict(lambda: 'Huh?') #可以直接使用lambda

"""
計數器 page 124 -126
"""
#int()可以製作計數器
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1 

for food, count in food_counter.items():
    print (food, count)
    
#如果一般狀況，food_counter是一般字典，需要做額外的事情
dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0 #預設為零
    dict_counter[food] += 1

#用Ｃounter來計算項目數量
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)

#most_common()會以降冪回傳所有元素，也可以指定數目，回傳最前面的count個元素
breakfast_counter.most_common()
breakfast_counter.most_common(1) # differnt output as last one

#可以結合兩個計數器用 +加號
lunch = ['bread', 'eggs', 'bacon']
lunch_counter = Counter(lunch)

breakfast_counter + lunch_counter

#早餐有午餐沒有的 = 早 - 午
#午餐有早餐沒有的 = 午 - 早
#可以用交集 = 早 & 午（值會提供比較少的那個）
#連集 = 早 | 午 （一樣的值會提供比較多的那個）

#使用OrderedDict()來排序，一般的不會按照順序回傳
from collections import OrderedDict
quotes = OrderedDict([
        ('Moe','A wise guy, huh?'),
        ('Laryy', 'Ow!'),
        ('Curly', 'Nyuk nyuk!')
        ])

#堆疊 + 序列 == deque(念deck) page 127
def palindrome(word): #palindrome回文
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True #這邊是要展示deque的功用

def another_palindorme(word):
    return word == word[::-1] #不用再寫if跟else

"""
使用itertools 來迭代程式結構 page 128
特殊的函示，會一次回傳一個
"""
#chain會逐一經過引數，就像他們是可迭代的單一項目
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

#cycle()無限循環器
for item in itertools.cycle([1, 2]):   
    print (item) #要怎麼break?

#accumulate()會計算累計的值
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

#可以在accumulate()的第二個引述提供函式（必須要有兩個引述），提供的函式會取代加法
def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print (item)

#用pprint()印出好看的結果
from pprint import pprint
print (quotes)           
pprint(quotes) #會試著排列元素

"""
Pypi http://pypi.python.org
github https://github.com/Python
readthedocs https://readthedocs.org/
"""

#Q1 zoo.py
#Q2 zoo as menagerie    
#Q3 from zoo import hours
#Q4 import hours as info
#Q5 plain = {'a': 1, 'b': 2, 'c': 3}
#Q6 fancy = OrderedDict(plain)
#Q7 dict_of_lists = defaultdict(list)




    