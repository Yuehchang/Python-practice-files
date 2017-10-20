#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 21:00:58 2017

@author: changyueh
"""
#用list()可以將其他資料轉換成串列 page 47

#1. 字串轉換      
list('cat') # output => ['c', 'a', 't']

#2. tuple轉換
a_tuple = ('ready', 'fire', 'aim')
list(a_tuple) # output => ['ready', 'fire', 'aim']

#3. slipt()可以切割字串
birthday = '11/06/1992'
birthday.split('/') # output => ['11', '06', '1992'] # 如果有兩個//則返回會有空格 #split(裡面分隔的條件可以很多樣式，字也可以)

#增減與結合串列
#1. append()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo') # output => ['Groucho', 'Chico', 'Harpo', 'Zeppo']

#2. extend() or +=
others = ['Gummo', 'Karl']
marxes.extend(others) # output => ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'karl']

marxes += others # output => same as extend

marxes.append(others) # output => ['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'karl']] 被加成一個串列，而不是字符

#3. insert()與位移值來加入
marxes.insert(3, 'Gummo') # output => ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']

#4. del，需要有位移值
del marxes[-1] # output => ['Groucho', 'Chico', 'Harpo', 'Gummo']

#5. remove()，不需要位移值
marxes.remove('Gummo') # output => ['Groucho', 'Chico', 'Harpo', 'Zeppo']

#6. pop()，用位移值取得項目並從串列中刪除
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop() # output => 'Zeppo'
marxes # output => ['Groucho', 'Chico', 'Harpo']
marxes.pop(1) # output => 'Chico'
marxes # output => ['Groucho', 'Harpo']

"""
當資料進入資料庫時，有兩種方式可輸入與輸出資料 
1. LIFO(後進先出) append()增加資料，pop()移除資料
2. FIFO(先進先出) append()增加資料，stack.pop(0)移除資料
page 52，可好好善用
"""

#index()找尋位移值
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.index('Chico') # output => 1

#用 "in" 測驗值是否存在於串列之中
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
'Croucho' in marxes # output => True
'Bob' in marxes # output => False

#join and split page 53 - 54
friends = ['Harry', 'Harmione', 'Ron']
separator = '*'
joined = separator.join(friends)
separated = joined.split(separator) #可以看出join和split的用法

#sort()就地排列 // sorted()會排列串列，但需要回傳複本
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
sorted_marxes = sorted(marxes)

marxes.sort() #直接改變原始的值

"""
當資料混合多種類型，Python運算式會自動將他們轉換 page 55
預設的排序是升冪，加入引數 reverse = True 變成降冪
"""

#串列複製到一個獨立的新串列 1. copy() 2. list()轉換函示 3. slice[:]
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:] #b, c, d都是a的複本，但是改變a的值不會影響到其餘三個，如果是a=b，改變a值就會引響b值

a[0] = 'integer lists are boring' # output => ['integer lists are boring', 2, 3]，其餘的都是[1, 2, 3]

#####################################

#Tuple  
empty_tuple = () #create a empty tuple

one_marx = 'Groucho', #create one or multi-element, need to add ',' at each end of the element 

marx_tuple = 'Groucho', 'Chico', 'Harpo' #最後一個不用逗號，加不加括號都可以

#unpacking 
marx_tuple = 'Groucho', 'Chico', 'Harpo'
a, b, c = marx_tuple # output => a = 'Groucho', b = 'Chico', c = 'Harpo' 

# turn LIST into tuple 
marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list) # output => ('Groucho', 'Chico', 'Harpo')

"""
Adventage of tuple
1. less memory space to store the data
2. 不會不小心破壞項目
3. 字典鍵
4. Named tuple = 簡化替代品
"""
#####################################

#Dictionary
empty_dict = {}

#i.g
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
dict(lol) # output => {'c': 'd', 'a': 'b', 'e':, 'f'}

#如果輸入錯誤，可以直接做更改
pythons = {
        'Chapman': 'Graham',
        'Cleese': 'John',
        'Idle': 'Eric'
        }

pythons['Gilliam'] = 'Gerry' #should be Terry not Gerry // 
#output => {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Gilliam': 'Gerry'}

#直接做更改
pythons['Gilliam'] = 'Terry' #output => {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Gilliam': 'Terry'}

#用update()來合併字典
others = { 'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others) # output => 新的會加上去 ＃如果有重複的值，第二個字典的值會勝出

#用del與鍵來刪除項目
del pythons['Marx'] #只要del鍵就可以，值也會一起del

#用clear()來刪除所有項目
pythons.clear() # output => {}

# 一樣可以用in來測試字典裡面有誰

#用[鍵]來取得一個項目 page 64

#用keys()來取得所有的鍵 => 但是回傳要變成串列要轉換 list( xx.keys() )
#用values()來取得所有的值 => list( xx.values() )
#用items()來取得所有的鍵/值對 => list( xx.items() ) => 每一個鍵與值都會回傳成tuple的形式
 
#####################################

#Set
empty_set = set() #{}會形成空字典，而非空集合
even_numbers = {0,2,4,6,8}
odd_numbers = {1,3,5,7,9}

#所以使用set()可以將串列，字串，tuple建立成集合，並丟棄重複的值
#將字典丟給set()，他只會用到鍵
#用in測試值，用到for & if語句，很不錯 page 69

"""
a = {1, 2} // b = {2, 3}
含有、交集 => a & b = a.intersection(b) output => {2}
聯集 => a|b = a.union(b) output => {1, 2, 3}
差集 => a - b = a.difference(b) output => {1}
還有許多：page 70
1. 互斥symmetric_difference() / ^
2. 其中是不是子集合 issubset() / <= 左是右的子集合
3. 真集合 < 第二個集合必須擁有第一個集合的所有成員
4. 超級合 issuperset() / >= 和子集合相反
5. 真超集合 >
"""

#Practice Part.1 page72
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'C;eese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

#1.製作tuple
tuple_of_lists = marxes, pythons, stooges
#2. 製作list
list_of_lists = [marxes, pythons, stooges]
#3. 製作dict
dict_of_lists = {'Marxes' : marxes, 'Pythons' : pythons, 'Stooges' : stooges}

"""
Practice Part.2 page73
"""
#Q1 5 years since i'm bron
year_lists = [1992, 1993, 1994, 1995, 1996]
#Q2 Third Birthday
year_lists[2]
#Q3 Oldest in the list
year_lists[len(year_lists)-1]
#Q4 thing lists
things = ['mozzarella', 'cin derella', 'salmonella']
#Q5 make the first letters Cap
things[1] = things[1].capitalize() #注意！！
#Q6 All Cap
things[0] = things[0].upper()
#Q7 remove the nonsense
things[2] = 'Nobel Prize'
#Q8 surprise list
surprise = ['Groucho', 'Chico', 'Harpo']
#Q9 turn last one into lower cap
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
#Q10 e2f dict
e2f = { 'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
#Q11 print value of walrus
e2f['walrus']
#Q12 f2e dict 注意！！！！！
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
#Q13 print chien
f2e['chien']
#Q14 make key set
e2f_key_dict = set(e2f.keys())
#Q15 life 
lifes = { 
        'animals' : {'cat' : ['Henri', 'Grumpy', 'Lucy'], 'octopi' : {} , 'emus' : {}},
        'plants' : {},
        'others' : {}
        }
#Q16 print topest keys
list(lifes.keys())
#Q17 print animals keys
list(lifes['animals'].keys())
#Q18 print animals values
lifes['animals']['cat']

"""
Good practice especially 
Q5
Q9 [::-1]
Q12 交換
Q15 
Q18
"""

