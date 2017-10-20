#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:23:23 2017

@author: changyueh
"""
import numpy as np

#創建ndarray
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2
arr2.ndim
arr2.shape

np.zeros(10) #都是零的一列
np.zeros((3, 6)) #shape = (3,6)，都是零的3列6行
np.arange(15) #一列從0到14
np.identity(3) #對角為1的矩陣

#ndarray的數據類型dtype、page86/87有更多類型介紹
arr3 = np.array([1, 2, 3], dtype=np.float64)
arr4 = np.array([1, 2, 3], dtype=np.int32) #可以儲存成不同的數據類型

##astype轉換類型
arr5 = np.array([1, 2, 3, 4, 5]) #type: int64
float_arr5 = arr5.astype(np.float64) #type: float64 

numeric_strings = np.array(['1.24', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(np.float) #直接轉換成數值
               
#數組(array)與向量之間的運算
arr6 = np.array([[1., 2., 3.], [4., 5., 6.]])
arr6                      
arr6 * arr6
arr6 - arr6 

#索引與切片                      
arr7 = np.arange(10)
arr7
arr7[5]
arr7[5:8]
arr7[5:8] = 12 #可以直接改變內部數值
arr7 #5-8改變成12了

##如果把數組中的一段指派出來，原數組會跟著變動，並不是複製出新的array
arr7_slice = arr7[5:8]
arr7_slice[1] = 12345
arr7
arr7_slice[:] = 64
arr7 #如果是要複製就需要使用arr7[5:8].copy()

arr8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr8[2] #在二維以上的數組時，切片即是不同的向量組
arr8[2][1]
arr8[2, 1] #兩式相等

##索引跟list差不多
arr7[1:6] #另有高維度的索引 page91、圖4-2

##布林索引
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)

names == 'Bob' #回傳的值也是項量化的Boolean
data[names == 'Bob'] #因為0, 3為真，所以等於返回0跟3的值，但長度必須跟數組值一致

data[names == 'Bob', 2:] #可以跟切片混用

names != 'Bob'
data[-(names == 'Bob')] #負號跟!=是一樣的

mask = (names == 'Bob') | (names == 'Will')
mask #新的一個布林向量
data[mask]

data[data < 0] = 0 #將負數設定成零
data
data[names != 'Joe'] = 7 #利用布林來變化整行數值也很簡單
data

##花式索引
arr9 = np.empty((8, 4))
for i in range(8):
    arr9[i] = i
arr9
arr9[[4, 0, 3, 6]] #指定順序的切片

arr10 = np.arange(32).reshape(8,4)
arr10[[1, 5, 7, 2], [0, 3, 1, 2]] #得到是單個
#arr10[[1,0], [5,3], [7,1], [2,2]] 無法找
arr10[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
arr10[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]

#數據可以轉置
arr11 = np.arange(15).reshape((3,5))
arr11
arr11.T

arr12 = np.random.randn(6,3)
np.dot(arr12.T, arr12)                 

#通用函數：快速的組數函數，函數都在page99/100找得到
arr13 = np.arange(10)
np.sqrt(arr13)
np.exp(arr13) #以上都是unary ufunction

x = np.random.randn(8)
y = np.random.randn(8)
x                      
y                      
np.maximum(x, y)                      

#利用array進行數據處理
##practice1
points = np.arange(-5, 5, 0.01) #一千個相等的點
xs, ys = np.meshgrid(points, points)

import matplotlib.pyplot as plt

z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()      
plt.title('Image plot if $\sqrt{x^2 + y^2}$ fir a grid of values') 

##將條件邏輯表述為數組運算
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])               
cond = np.array([True, False, True, True, False]) 

result = np.where(cond, xarr, yarr) #True為xarr, False為yarr                    
                          
#pratice2
arr14 = np.random.randn(4,4)
arr14  
np.where(arr14 > 0, 2, -2)
np.where(arr14 > 0, 2, arr14) #如果有兩種cond的複雜邏輯運算，可參見page103

#數學和統計方法
##基本數組統計方法page104/105
arr15 = np.random.randn(5,4)

arr15.mean()
np.mean(arr15)
arr15.sum()
arr15.mean(axis=0) #axis=1為橫相加、axis=0為縱相加

##用於布林數組的方法
Boolean = np.array([True, False, True, True])
Boolean.sum() #利用上述算法會直接把布林值變成1跟0

Boolean.any() #偵測是否有一個或一個以上的True
Boolean.all() #偵測是否全是True ##也可用於一般數值，零以外的都是歸類True         

#排序
sort()

#集合邏輯，page107表4-6中友數組的集合運算
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names) #一種值只返回一次

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
np.unique(ints)

values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3]) #給予條件返回布林值

#用於文件的輸入與輸出 
arr16 = np.arange(10)
np.save("some_array", arr16) #可以存取成.npy的檔案，可以被np.load讀取
np.load("some_array.npy") #直接返回Array

np.savez('array_archive.npz', a=arr15, b=arr16) #可將多個數組保存在一個壓縮文件中
arch = np.load('array_archive.npz')
arch['b'] #加載後會得到一個類似字典的對象，但不會顯示在variable explorer中     

##存取文本文件，np.loadtxt / np.savetxt / np.genfromtxt都在page108/109

#線性代數，page110表4-7有常見的函數可以使用，都需要從numpy.linalg匯入
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])

x
y

x.dot(y) # = np.dot(x, y)

from numpy.linalg import inv, qr
x = np.random.randn(5, 5)
mat = x.T.dot(x)
inv(mat) #找出逆矩陣
mat.dot(inv(mat)) #在矩陣中自己dot自己的逆矩陣等於Identiy矩陣

#隨機數生成，page111/112表4-8有許多有用隨機產生變數之函數
samples = np.random.normal(size=(4, 4))
samples
       
##比較python內建跟np.random的速度差別
from random import normalvariate
N = 10000000
%timeit samples1 = [normalvariate(0, 1) for _ in range(N)]
%timeit np.random.normal(size=N)

##practice1 Random Walk!
import random
position = 0
walk = [position]
step = 1000
for i in range(step):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

nsteps = 1000 #先設定投擲1000次數量
draws = np.random.randint(0, 2, size=nsteps) #產生在0與1之間隨機分布的1000個整數值
steps = np.where(draws > 0, 1, -1) #將上面的0、1轉換成1跟-1
walk = steps.cumsum() #做出隨機漫步的結果
(np.abs(walk) >= 10).argmax() #找出什麼時間點是第一次進入條件（正負10），前面會返回一組布林數組，後面會找出第一個最大值（因為都是1所以第一個最大值就是我們要找的）

##practice2 Random Walks!
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1) #如果cumsum裡面沒有輸入1，數值會累加

hits30 = (np.abs(walks) >= 30).any(1)#使用any的原因是不一定所以都達到30 or -30，利用any返回布林值找出有跟沒有的array
hits30
hits30.sum() #找出有多少個達到30 or -30
cross_timing = (np.abs(walks[hits30]) >=30).argmax(1) #利用hits30的布林值（為True）找出符合條件的數組最快到達正負30的值
cross_timing.mean() #找出平均值

#還可以利用不同的分佈去產生漫步數據


                     
            