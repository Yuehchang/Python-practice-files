#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 08:11:40 2017

@author: changyueh
"""

#用class來定義類別 page 134
#空類別
class Person():
    pass #等同return一樣要說明是空的

someone = Person() #用類別建立物件，用法如同函式

#practice 
class Person():
    def __init__(self):
        pass #這個也無法建立一個真的能做事的物件

class Person():
    def __init__(self, name):
        self.name = name
 
"""       
繼承 page 136 使用既有的類別來建立一個新的類別，但加入一些新的東西
"""
#原本的類別：父系(parent)、超類別(superclass)、基礎類別(base class)
#新類別：子系(child)、子類別(subclass)、衍生類別(derived class)

class Car():
    pass

class Yugo(Car):
    pass #子類別
    
give_me_a_car = Car()
give_me_a_yugo = Yugo()#子類別是父類別的特例，give_me_a_yugo的物件是Yugo類別的一個特例

#practice
class Car():
    def exclaim(self):
        print ("I am a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car() #give_me_a_car.exclaim() => output = "I'm a Car!"
give_me_a_yugo = Yugo() #give_me_a_yugo.exclaim() => output = "I'm a Car!"

#覆寫方法 => 跟改一些行為
class Car():
    def exclaim(self):
        print ("I am a Car!")
        
class Yugo(Car):
    def exclaim(self): #雖然都是exlaim，但是覆寫了內容
        print ("I'm a Yugo! Much like a Car, bur more Yugo-ish!")

#practice 
class Person():
    def __init__(self, name):
        self.name = name
class MDPerson(Person):
    def __init__(self, name):
        self.name = 'Doctor ' + name
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

#添加方法，可加入父類別沒有的
class Car():
    def exclaim(self):
        print ("I'm a Car!")
class Yugo(Car):
    def exclaim(self):
        print ("I'm a Yugo! Much like a Car, but more Yugo-ish!")
    def need_a_push(self):
        print ("A little help here?")

#用super來讓父系幫助你
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name) #用super就直接取得父類別的Person的定義
        self.email = email #可以直接新定義，但是繼承的好處是，如果之後person改變，這邊就直接改變
        
#self防衛 page141
#使用特性來取得屬性質與設定它 page141 可以再看看！！！！！！！！
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print ('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print ('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)
    
#使用裝飾器
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

#practice p143
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

#搞砸私用名稱
"""
Python有一個命名規範：
在開頭使用雙底線 => 對於不能被類別定義是之外的程式看到的屬性
"""
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name #這種命名規範不會變成私有，但是可以有效地保護

#方法類型 類別屬性 vs 物件實例屬性 page146 可以再看看！！！！！！！！
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, 'little objects.')

#Duck Typing 
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'
        
class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'
class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

#Python可以執行不同類別裡面的相同函示
def who_says(obj):
    print(obj.who(), 'says', obj.says)

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return "I'm ok" #儘管這個類別跟前面三個Quote完全沒關係，因為有who, says一樣可以用who_says()印出相同結果

#特殊方法
#practice1 page149
class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2): #改成這樣就不用引用函式，直接"=="就好了，測試是否相等就用__eq__
        return self.text.lower() == word2.text.lower()
"""
p150頁有兩種魔術方式可以查詢
"""

#__str__() // __reper__()的用法
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, text2):
        return self.text.lower() == text2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("' + self.text + '")'
        
#組合
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print("This duck has" , self.bill.description, "bill and a", self.tail.length, 'tail.' )
        
class Duck2():
    def __init__(self, text):
        self.text = text 
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.text
    def about(self, text2):
        print("This duck has" , self.text, "bill and a", text2, 'tail.' ) #效果跟上面一樣

#提供具名字串
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long') # output => Duck(bill='wide orange', tail='long') // duck.bill就會直接呼叫bill的值

#利用字典做具名字串
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts) # output = Duck(bill='wide orange', tail='long')

#具名tuple是不可變的，但是可以更換欄位的值
duck3 = duck2._replace(tail='magnificent', bill='crushing')

#Q1
class Thing(): #class Thing: 不用括號
    pass
print (Thing）# output => <class '__main__.Thing'>

example = Thing()
print(example) # output => <__main__.Thing object at...>

#Q2
class Thing2:
    def letters(self):
        print ('abc') #incorrect 

class Thing2:
    letters = 'abc'

#Q3
class Thing3():
    def letter():
        print('xyz') #incorrect
    
class Thing3:
    def __init__(self):
        self.letters = 'xyz' # a = Thing3 (不對) // a = Thing3()
#Q4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
Hydrogen = Element('Hydrogen', 'H', 1)
print(Hydrogen.name, Hydrogen.symbol, Hydrogen.number)

#Q5
p_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
#First
hydrogen = Element(p_dict['name'], p_dict['symbol'], p_dict['number'])
#Second
hydrogen = Element(**p_dict)
print(hydrogen.name)

#Q6 
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name, 'is same as', self.symbol, 'and its number is', self.number)
Hydrogen = Element('Hydrogen', 'H', 1)
Hydrogen.dump()

#Q7
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
       return ('name: %s, symbol: %s, number: %s' % (self.name, self.symbol, self.number))
Hydrogen = Element('Hydrogen', 'H', 1)
print(Hydrogen) #Ｑ6裡面打的句子打的不能用在__str__，不接受tuple

#Q8     
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property #我原本沒加
    def get_name(self):
        return self.__name
    @property #這就是getter變成可以私用
    def get_symbol(self):
        return self.__symbol 
    @property #沒有加的話，不能直接當屬性使用
    def get_number(self):
        return self.__number
Hydrogen = Element('Hydrogen', 'H', 1)
Hydrogen.get_name

#Q9
class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'

bear = Bear()
print(bear.eats())
rabbit = Rabbit()
print(rabbit.eats())
octothorpe = Octothorpe()
print(octothorpe.eats())

#Q10 
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'
class Robort:
    laser = Laser()
    claw = Claw()
    smartphone = SmartPhone()
    def does(self):
        print("This Robort have three functions as a laser which can %s, two claws which can %s and one smartphone which can %s." %
              (self.laser.does(), self.claw.does(), self.smartphone.does()))
Steven = Robort()       
Steven.does()

#有點不一樣
class Robort:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return """ This ..."""
Steven = Robort()
print(Steven.does())
