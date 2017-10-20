#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:57:41 2017

@author: changyueh
"""
type() #瞭解()的物件類型
 
# / 浮點除法 ＝> 7/2 => 3.5 
# // 整數除法 ＝> 7/2 => 3 (捨去)
# % 餘數 ＝> 7/2 => 1

a -= 3 <==> a = a - 3 #兩個式子是一樣的
a += 3 <==> a = a + 3
a *= 3 <==> a = a * 3

divmod() #可以回傳商及餘數 page 25

#基數 二進位 0b/0B // 八進位 0o/0O // 十六進位 0x/0X

0b10 #2
0o10 #8
0x10 #16

#類型轉換 page 27
# 整數
int() #轉變成整數，捨棄小數
int(True) #轉變成 1
int(False) #轉變成 0

int('-99') #轉換只含數字的字串
int('99.89') #無法處理有小數的字串

#Boolean與數字相加時會自動變成 0 or 1
True + 1 # = 2

#浮點數
float() #()裡面中如是整數，會自動變成增加“點零”

#用str()轉換資料類型 page 33
str() #數值轉變成字串

# \ => 轉義
palinedrome = 'A man, \nA plan, \nA canal, \nPanama.'
print(palinedrome)
# \n 代表換行

print('\tabc')
print('a\tbc')
# \t 代表對齊

testimony = "\"I did noting!\" he said. \"Not that either! Or the other thing.\""
print(testimony)
# \' or \" 代表引號   

fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'" # 必須利用\"代替，不然字串會斷掉
#需要反斜線就打兩次 \\

# 用*來複製
strat = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye.'
print(strat + strat + middle + end)
 
#Slice的使用
[:] #從開始到結束
[start :] #從start到結束
[: end] #從頭到(end-1)
[start : end] #從start到(end-1)
[start : end : step]

#如果沒有指定start or end就會從0開始，-1結束

#把玩字串 page 40-41
len()
startswith() #找出字串的開頭，括號內輸入“值”
endswith() #與上述相反
find() #找出括號內的值，第一次出現的位移植
rfind() #最後一次的位移植
count()
isalnum()

#大小寫與對齊 page 41
strip("char") #可以移除內容
capitalize() #第一個字改為大寫
title() #全部字的第一個字改為大寫
upper() #全部大寫
lower() #全部小寫
swapcase() #大小寫對掉
center(30) #在30個字元中對齊，數值可隨時替換
ljust(number) #靠左對齊
rjust(number) #靠右對齊

# replace()做簡單替換
replace('char1', 'char2') #用char2替換char1，但是只會替換第一個
replace('char1', 'char2', 100) #等同效果，替換100個
"""
如果要替換全部的字，或複雜的替換，需使用“正規表達式”，第七章會介紹
"""

