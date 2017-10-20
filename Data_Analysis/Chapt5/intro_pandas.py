#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:56:50 2017

@author: changyueh
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#Pandas的數據結構介紹
##Series
yc = Series([4, 7, -5, 3]) #如同array一樣但多了index
yc.values
yc.index

yc1 = Series([9, 4, 5, 3], index=['t', 'a', 'n', 'g']) #標記索引
yc1.index
yc1['t'] #跟array不同，可以利用index找單個或多個值 = yc1[0]

'b' in yc1
't' in yc1 #此兩者是字典的用法，Series也可以用

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
yc2 = Series(sdata)
yc2 #可以直接利用字典來創建Series

stats = ['California', 'Ohio', 'Oregon', 'Texas']
yc3 = Series(sdata, index=stats)
yc3 #利用list來建立index，會依照有的index創立Series，如果index對照的內容沒有值，則顯示nan(not a number)

pd.isnull(yc3)
pd.notnull(yc3) #利用此函數檢視缺失數據
yc3.isnull() #Series也有此函數可以查看

yc2
yc3
yc2 + yc3 #自動對齊不同的索引數據，兩個Series都有的值會互相相加，如果有只有一邊有合併產生nan     

yc3.name = 'population'
yc3.index.name = 'stats'
yc3    

yc.index = ['y', 'u', 'e', 'h'] #index可以直接做更改

##DataFrame，許多種可以輸入的方式page123表5-1
#構建的方式有很多，最常用的是一種利用等長列表或是NumPy數組組成的字典
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data) #自動加上index，並且全部有序排列

DataFrame(data, columns=['year', 'state', 'pop']) #如果有說明columns的排列順序，會依照此順序排列
         
frame1 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame1 #跟Series一樣，如果輸入的列找不到，就會產生nan
frame1['state'] #可以利用跟Dict一樣的方式獲取一個Series
frame1.loc['three'] #除上述之外加上loc可以從index找

frame1['debt'] = 16.5, 17.5, 18.5, 17, 18 #如果只輸入一個，就全部都一樣，如果要數入多個必須跟row的長度一樣個數才行
frame1['debt'] = np.arange(5.)      
frame1['debt'] = Series([-1.2, -1.5, -1.7], index=['two', 'three', 'five']) #如果導入一個Series，填上index其他值就會變成nan
frame1['eastern'] = frame1.state == 'Ohio' #可以新建新的列
del frame1['eastern'] #利用del刪除

#另一種方式是嵌套字典
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002:3.6}}
frame2 = DataFrame(pop)
frame2
frame2.T
frame2.index.name = 'year'; frame2.columns.name = 'state'
frame2
frame2.values #二維的ndarray形式返回DataFrame中的數據

##索引對象index，page125表5-2展現pandas中主要的Index對象、page126表5-3說明Index的方法與屬性
yc4 = Series(range(3), index=['a', 'b', 'c'])
index = yc4.index
index
index[1:]
###index[1] = 'b' #不可以修改，這樣可以在多個數據結構之間共享

index = pd.Index(np.arange(3)) #不是variables
yc5 = Series([1.5, -2.5, 0], index=index)
yc5.index is index #index是重要主成部分

#基本功能
##重新索引reindex，page129有其函數的參數可參考
yc6 = Series([0, 8, 1, 3], index=['t', 'a', 'n', 'g'])
yc6
yc6_1 = yc6.reindex(['c', 'h', 'a', 'n', 'g'])
yc6_1 #沒有的值就會出現nan
yc6.reindex(['c', 'h', 'a', 'n', 'g'], fill_value=0)

yc7 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
yc7.reindex(range(6), method='ffill') #假如0有值，就會把0後面新增的沒有值的內容補齊，以0為準，前向填充
yc7.reindex(range(6), method='bfill') #後填上去

frame3 = DataFrame(np.arange(9).reshape((3,3)), index=['a', 'c', 'd'],
                   columns=['Ohio', 'Texas', 'California'])       
frame3 
frame3_1 = frame3.reindex(['a', 'b', 'c', 'd']) #可以橫向更改
frame3_1 
frame3_1.reindex(columns=['Texas', 'Utah', 'California']) #也可以縱向更改，使用columns關鍵詞
frame3.reindex(index=['a', 'b', 'c', 'd'], columns=['Texas', 'Utah', 'California']) #可以同時更改

##丟棄指定軸上的項
yc8 = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])              
yc8.drop('c')
yc8.drop(['c', 'd']) #可以丟棄一個或多個

frame4 = DataFrame(np.arange(16.).reshape((4,4)),
                   index=['Ohio', 'Colorado', 'Utah', 'New York'],
                   columns=['one', 'two', 'three', 'four'])
frame4.drop(['Ohio'])
frame4.drop(['one', 'two'], axis=1)

##索引、選取、過濾
yc9 = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
yc9['b'] # = yc9['1']
yc9[2:4]
yc9[['c', 'd']] # = yc9[[2, 3]]
yc9[yc9 < 2] #索引值不一定是整數，可以為index or 條件

yc9['b':'c'] #用標籤的切片運算，其末端有包含
yc9['b':'c'] = 5
yc9 #可以利用上述直接設置數值

#DataFrame的索引細節在page132/133的表5-6
frame5 = DataFrame(np.arange(16.).reshape((4,4)),
                   index=['Ohio', 'Colorado', 'Utah', 'New York'],
                   columns=['one', 'two', 'three', 'four']) 
frame5        
frame5['two']
frame5[['three', 'two']]
frame5[:2]
frame5[frame5['three'] > 5]
frame5 < 5 #返回布林值
frame5[frame5 < 5] = 0
frame5 #利用frame5<0找出True&False，並在上面的式子設定返回小於5就等於0
frame5.loc['Colorado', ['two', 'three']] 
frame5.ix[['Ohio', 'Utah'], [3, 0, 1]] #利用ix可以更靈活地找子集
frame5.ix[frame5.three > 7, :3] 

##算術運算和數據對齊
#Series跟DataFrame中重疊的行or行列才會合併，為重疊的值就是nan
frame6_1 = DataFrame(np.arange(12.).reshape((3,4)), columns=list('abcd'))
frame6_2 = DataFrame(np.arange(20.).reshape((4,5)), columns=list('abcde'))

frame6_1 + frame6_2
frame6_1.add(frame6_2, fill_value=0) #傳入frame6_2的數值與一個fill_value參數
frame6_1.reindex(columns=frame6_2.columns, fill_value=0) #再重新索引時，可以指定填充

#DataFrame跟Series之間的運算
yc10 = np.arange(12.).reshape((3, 4))
yc10
yc10 - yc10[1] 

frame7 = DataFrame(np.arange(12.).reshape((4, 3)),
                   columns=list('abc'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series_7 = frame7.iloc[0]
frame7 - series_7 #每一層都會減掉，叫做廣播broadcasting
series_7_1 = frame7['b']
frame7.sub(series_7_1, axis=0)

##函數應用與映射
frame8 = DataFrame(np.random.randn(4, 3),
                   columns=list('bde'),
                   index=['Ohio', 'Utah', 'Texas', 'Oregon'])
frame8
frame8.abs() # = np.abs(frame8) 取絕對值

f = lambda x: x.max() - x.min()
frame8.apply(f)
frame8.apply(f, axis=1)   

def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame8.apply(f) #傳遞進去的函數可以是多個值組成的Series

f = lambda x: '%.2f' % x
frame8.applymap(f) #這邊特別使用applymap!
frame8['b'].map(f) #Series有一個元素級函數的map用法，所以上述也要用map 

#排序和排名  
yc11 = Series(np.arange(4), index=list('dabc'))
yc11.sort_index() #自動是升序

frame9 = DataFrame(np.arange(8).reshape((2, 4)),
                   index=['three', 'one'],
                   columns=['d', 'a', 'c', 'b'])               
frame9.sort_index()
frame9.sort_index(axis=1) #columns排列

frame9.sort_index(axis=1, ascending=False)

yc12 = Series([7, 4, -3, 2])
yc12.sort_values() #若按照值對Series進行排序，可以利用order

yc12_1 = Series([7, 4, np.nan, -3, np.nan, 2])
yc12.sort_values() #好像這個版本中不會返回nan

frame10 = DataFrame({'b':[4, 7 ,-3, 2],
                     'a':[0, 1, 0, 1]})
frame10
frame10.sort_index(by='b')     
frame10.sort_values(by='b') #如果想一個或多個列中的值進行排序，可用by
frame10.sort_values(by=['a', 'b'])

yc13 = Series([7, -5, 7, 4, 2, 0, 4])
yc13.rank() #排名在默認條件下，會通過平均排名來返回值
yc13.rank(method='first') #會根據值在原數據中出現的順序給出排名
yc13.rank(ascending=False, method='max')
yc13.rank(ascending=False, method='min') #這個比較合理，同樣的數值排名一樣，其餘的會後一號排名

frame11 = DataFrame({'b': [4.3, 7 ,-3, 2],
                     'a': [0, 1, 0, 1],
                     'c': [-2, 5, 8, -2.5]})               
frame11
frame11.rank()
frame11.rank(axis=1)

##帶有重複值的軸索引
yc14 = Series(np.arange(5), index=list('aabbc'))
yc14
yc14.index.is_unique #index不為唯一
yc14['a'] #會返回兩個

#匯總和計算描述統計，page144表5-10有詳細的描述與匯總統計
frame12 = DataFrame([[1.4, np.nan], [7.1, -4.5],
                     [np.nan, np.nan], [0.75, -1.3]],
                    index=list('abcd'),
                    columns=['one', 'two'])
frame12
frame12.sum() #把nan計算成0
frame12.sum(axis=1) #利用index來計算axis=1, 利用columns來計算axis=0
frame12.mean(axis=1, skipna=False) #把nan計算當中，所以a就會展現nan
frame12.describe() #利用describe會有多個匯總統計

yc15 = Series(list('aabc')*4)
yc15
yc15.describe()

#相關係數與共變異數
"""
import pandas_datareader.data as web
all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOGL']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2010', '1/1/2017') 
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
volumn = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
"""
#其中get_yahoo_data的URL已經失效，所以無法獲取資料
#corr() / cov()的用法在page145/146

##唯一值、值計數與成員資格額，page148表5-11有介紹
yc16 = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = yc16.unique()
uniques #返回的唯一值是不排序的，uniques.sort() => type:nontype 沒有東西返回
yc16.value_counts() #計算頻率，算是pandas頂級方法 => pd.value_counts(yc16.values, sort=False)可以利用在數組(yc16.values是array)或是序列

mask = yc16.isin(['b', 'c'])
mask #返回boolean
yc16[mask] #可以當條件搜尋

frame13 = DataFrame({'Q1': [1, 3, 3, 4, 4],
                     'Q2': [2, 3, 1, 2, 3],
                     'Q3': [1, 5, 2, 4, 4]})
frame13    
frame13.apply(pd.value_counts).fillna(0) #結果是出現各個數值的頻率table

#處理Missing Data，page149表5-12有NA的處理方法
string_data = Series(['aardvark', 'artichoke', np.nan, 'avovado'])
string_data
string_data.isnull()
string_data[0] = None
string_data.isnull() #Python內置的None也會被當做NA處理

##濾除缺失數據
yc17 = Series([1, np.nan, 3.5, np.nan, 7])
yc17.dropna() # => yc17[yc17.notnull()]

from numpy import nan as NA
frame14 = DataFrame([[1., 6.4, 3.], 
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
frame14.dropna() #DF默認drop任何有NA的row & columns
frame14.dropna(how='all') #只丟棄全部都是NA的row
frame14.dropna(axis=1, how='all') #只丟棄全部是NA的columns

frame15 = DataFrame(np.random.randn(7, 3))
frame15.loc[:4, 1] = NA; frame15.loc[:2, 2] = NA
frame15
frame15.dropna(thresh=3) #設立閾值3，有三個以上的不是nan值的rows才會留下來

##填充缺失數據，page152/153表5-13有fillna的參數
frame15
frame15.fillna(0)
frame15.fillna({1: 0.5})

frame15.fillna(method='bfill', limit=2) #對reindex有效的ffill&bfill也可以利用

yc18 = Series([1., NA, 3.5, NA, 7])
yc18.fillna(yc18.mean())

##層次化索引
yc19 = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
yc19 #有兩層的index
yc19.index
yc19['b'] #可以更方便選取子集
yc19['b':'c']
yc19.loc[['b', 'd']]
yc19[:, 2] #可以在內存中進行選取
yc19.unstack()
yc19.unstack().stack()

frame16 = DataFrame(np.arange(12).reshape((4, 3)), 
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
frame16
frame16.index.name=['key1', 'key2']
frame16['Ohio']

#重排分級順列
frame16.swaplevel(0 ,1) #page156的命名無法找到，在找原因
frame16.sort_index(level=0) #對單個級別進行排序
frame16.swaplevel(0 ,1).sort_index(level=0)

#使用DataFrame的列
frame17 = DataFrame({'a': range(7),
                     'b': range(7, 0, -1),
                     'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 
                     'd': [0, 1, 2, 0, 1, 2, 3]})
frame17
frame17.set_index(['c', 'd'])
frame17.set_index(['c', 'd'], drop=False)


