#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:11:48 2017

@author: changyueh
"""
# 用 “＃” 當作註解

# 用 "\"來延續多行
alphabet = ''
alphabet += 'abcd'
alphabet += 'efgh'

alphabet1 = 'abce' + \
        'efgh' + \
        'ijkl' 
        
# if elif else 
"""
practice 1:
furry = True / small = True => cat 
furry = True / small = False => bear 
furry = False / small = True => shink
furry = False / small = False => human
"""
furry = True 
small = True 

if furry:
    if small:
        print ('cat')
    else:
        print ('bear')
else:
    if small:
        print ('shink')
    else: 
        print ('human') #兩個就用 if / else 
        
# 三個就用 if / elif / else 
# 比較運算式 == != < <= > >= in 
# 下列視為False => None / 0 / '' / [] / {} / () / set()

"""
迭代器
"""
# while
# 用while來重複執行
count = 1 
while count <= 5:
    print (count)
    count += 1

# 用break來取消
while True:
    stuff = input("String to capitalize [type q to exit]: ")
    if stuff == 'q':
        break
    print (stuff.capitalize())

# 用continue來跳過
while True:
    value = input("Integer, please[q to exit]: ")
    number = int(value)
    if number % 2 == 0:
        continue
    if value == 'q':
        break
    print (value, 'square is', number * number)
    
# 用else來檢查中斷
numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print ('Found even number', number)
        break
    position += 1 
else:
    print('No even number found')
    
# for
#用for完成上面的例子
for number in numbers:
    if number % 2 == 0:
        print ('Found even number', number)
        break
    else:
        print ('No even number found')

#迭送字典 - keys
accusation = {'room' : 'ballroom', 'weapen' : 'lead pipe', 'person' : 'Col. Mustard'}
for key in accusation: # or, for card in accusation.keys()
    print (card)
# values
for value in accusation.values():
    print (value)
# key and values
for item in accusation.items():
    print (item) #output => ('room', 'ballroom'), ('weapen'..)
#設定兩個變數，一個給key、一個給value
for key, value in accusation.items():
    print ('Card', key, 'has the contents', value) 

#一樣可以用break使跳出迴圈，用法和while一樣
#一樣可以用continue跳過
#一樣可以使用else
cheeses = []
for cheese in cheeses:
    print ('This shop has some lovely', cheese)
    break
else:#可以想成for在搜尋東西，沒有搜到就會啟動else
    print ('There is not much of a cheese shop, is it?')

#用zip來迭代多個序列
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'apple', 'mango']
drinks = ['coffee', 'tea', 'milk']
desserts = ['tiramisu', 'pie', 'cheese cake', 'ice cream'] #最後不會印出ice-cream除非我們加長其他串列
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print (day, ': drink', drink, '- eat', fruit, '- enjoy', dessert)

#zip()也可以將同一個位移值的兩項目，做成list, dict 
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi' #tuple
list( zip(english, french) )
dict( zip(english, french) )
tuple( zip(english, french) )

#range => 讓你不用儲存數字列佔記憶體，並建立廣大的搜索範圍
#range(start, stop, step) same as slice() / stop value = actually value + 1 /going backward = -1
list( range(0,3) ) #可以產生[0, 1, 2]的串列

"""
生成器
結合迴圈與條件測試器：不在是初階程度了
"""
#串列生成式 [運算式 for 運算式 in 可迭代項目]
#1. 舊方法
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
#2. 迭代法
number_list = []
for number in range(1,6):
    number_list.append(number)
#3. 直接用range()
number_list = list(range(1,6))
# 4. python風格
number_list = [number for number in range(1,6)] #第一個number是運算式
number_list = [number - 1 for number in range(1,6)] #第一個可作運算

#製作list[1,3,5]只有奇數的
odd_list = [odd for odd in range(1,6) if odd % 2 == 1]

odd_list = []
for odd in range(1,6):
    if odd % 2 == 1:
        odd_list.append(odd) #傳統形式
#可以在生成式中，使用兩組以上的for
rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print (row, col)#舊式的嵌套迴圈

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols] #製作一串(row,col)的tuple
for cell in cells:
    print (cell)

for row, col in cells:
    print (row, col) #tuple unpacking 從每一個tuple中拉出row與col值

#字典生成式 {鍵運算式：值運算式 for 運算式 in 可迭代項目}
#practice
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts = {letter: word.count(letter) for letter in set(word)} # python風格

#集合生成式 {運算式 for 運算式 in 可迭代項目}

"""
函式
1.目的為重複使用的程式
2.可以做兩件事情，定義函數、呼叫它
"""
#首先將def()裡面的括號放東西
def echo(anything):
    return anything '' anything # invalid syntax
#呼叫的值為引數，建立時為參數
#None跟False有些為的差異，空值、空集合、空串列都是false，並不是None
def is_none(thing):
    if thing is None:
        print ('It is None!')
    elif thing:
        print ('It is True!')
    else:
        print ('It is False!')

#位置引數，值會被依序複製到對應的位置
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}#所以如果在menu裡面輸入得值，沒有依照順序的話，結果會完全不一樣
#關鍵字引數，用對應的參數直接指定引數，這樣就沒有順序上的問題
menu(wine='bordeaux', entree='beef', dessert='bagel') #可以位置和關鍵字混用，但是位置要放前

#指定預設參數值，可以先預設其一的參數，但是也可以提供引數
def menu_a(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

#practice page 98 // 預設會在還是被定義的時候計算，而不是在執行的時候
def buggy(arg, result=[]):
    result.append(arg)
    print(result) #預期每次輸入，都有新的list，但是會重複上次輸入的值

def buggy_correct(arg):
    result = []
    result.append(arg)
    return result #這樣就可以正常運作

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    return result #修正方式

#用*來收集位置引數，當在參數使用星號時，會將可變量的潛在引數群組話，變成參數變成一個tuple
def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', *args) #如果()內值超過兩個以上，剩餘的值都會被歸類到最後的print中

#用**來收集關鍵字引述，用雙個星號讓關鍵字引數群組化，變成一個字典
def print_kwargs(**kwargs): #kwargs是個字典
    print ('Keyword arguments:',kwargs) #print_kwargs(wine='melort', entree='mutton', dessert='macaroon') 

#文件字串，將文件指派給函式的定義式
def echo(anyting):
    'echo returns its input argument'
    return anyting
help(echo) #help()印出函數的文件字串
print(echo.__doc__) #只想看原始的文件字串，不想要有格式

#函數的多樣用法 page 101-102
#對函式傳入引數
def add_args(arg1, arg2):
    print (arg1 + arg2) #type(add_args) => class: 'function'
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2) #func-待執行的函式 / arg1-func的第一個引數 / arg2-func的第二個引數
run_something_with_args(add_args, 5, 9) # => 14

#practice - *args / **kwargs
def sum_args(*args):
    return sum(args)
def run_with_positional_args(func, *args): 
    return func(*args)

#def run_with_positional_argss(*args):
    #return sum(args) =>上述的可以隨機換函式，把多個函式結合 

run_with_positional_args(sum_args, 1, 2, 3, 4)

#內部函式，可以在函式裡面定義函式
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b) # output => a + b

#如果想在函式內部處理複雜的工作，內部函式非常實用
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

#Closure 
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2
##這邊非常的不懂，差別看得出來，一個是str一個是函數，但是回傳跟呼喚的點不太了解

#lambda()
#practice 
def edit_story(words, func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

#####上述可以用lambda()表示#########

edit_story(stairs, lambda word: word.capitalize() + '!')

"""
產生器generator page106
迭代產生器時，會記得上次被呼叫時所在的位置，並回傳下一個值
"""
#產生器函數，自己創造range()
def my_range(first=0, last=10, step=1):
    number = first 
    while number < last:
        yield number
        number += step
        
"""
裝飾器decorator page107
會接收一個函式，並回傳另一個函式
"""
def document_it(func):
    def new_function(*args, **kwargs):
        print ('Running function', func.__name__)
        print ('Positional arguments', args)
        print ('Keyword arguments', kwargs)
        result = func(*args, **kwargs)
        print ('Result:', result)
        return result
    return new_function

#手動應用裝飾器
def add_ints(a, b):
    return a + b
cooler_add_this = document_it(add_ints)

#第二種方式
@document_it
def multiple_ints(a, b):
    return a * b

#同一個函數可以有兩個以上的裝飾器
def square_it(func):
    def new_function(*arg, **kwarg):
        result = func(*arg, **kwarg)
        return result * result
    return new_function

#最靠近函數的裝飾會先執行 page109
#命名空間與範圍 page109-111
#在名稱中使用_與__ // 名稱：function.__name__ // 文件字串 function.__doc__

#使用try與except來處理錯誤，就算發生錯誤也要回報讓人知道有錯
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print ('Need a position between 0 and', len(short_list)-1, 'but got', position)

#practice 2 
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try: 
        position = int(value)
        print (short_list[position])
    except IndexError as err:
        print ('Bad index:', position)
    except Exception as other:
        print ('Something else broke:', other)

"""
Practice page115
"""
#Q1 
guess_me = 7
if guess_me < 7:
    print ('too low')
elif guess_me > 7:
    print ('too high')
else:
    print ('just right')
    
#Q2
guess_me = 7
start = 1
while True:
    if guess_me > start:
        print ('too low')
    elif guess_me == start:
        print ('found it!')
        break
    else:
        print ('oops')
        break
    start += 1

#Q3
number_list = [3 ,2 ,1, 0]
for number in number_list:
    print (number) 
    
#Q4
list = [number for number in range(10) if number % 2 == 0]

#Q5    
squares = {number: number * number for number in range(10)}

#Q6
sets = {number for number in range(10) if number % 2 == 1}

#Q7 用產生器回傳並用for迭代
for number in range(10):
    print ('Got', number) #not correct 

for string in ('Got %s' % number for number in range(10)):
    print (string)

#Q8 
def good():
    return ['Harry' ,'Ron', 'Hermione']

#Q9產生器
"""
def get_odds():
    odd = [number for number in range(10) if number % 2 == 1]
    print ("Third number in list:", odd[2]) #not corrrect
    return odd
get_odds()
"""
def get_odds():
    for number in range(1, 10 ,2):
        yield number 

for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("The third odd number is", number)
        break

#Q10
def test(func):
    def new_func(*args, **kwargs):
        print ('start')
        result = func(*args, **kwargs)
        print ('end')
        return result
    return new_func

#Q11 觀念要再加強
class OopsException(Exception):
    pass

try:
    raise OopsException
except OopsException:
    print ('Caught an Oops')
    
 #Q12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']   

for title, plot in zip(titles, plots):
    movie = {title: plot}
    print (movie) #會讓字典不是同一個

movie = dict(zip(titles, plots)) #correct anwser 

    

