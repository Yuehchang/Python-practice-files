#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:52:17 2017

@author: changyueh
"""
#合併數據庫
##數據庫風格的DF合併，page190/191表7-1有merge函數的詳細介紹
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
df1
df2 
pd.merge(df1, df2) #多對一的合併，c/d值沒有合併，inner join
pd.merge(df1, df2, on='key') #如果沒有指明就默認為同名的column，但是最好指名一下

df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})
pd.merge(df3, df4, left_on='lkey', right_on='rkey') #columns名不同也可以分別進行指定

pd.merge(df1, df2, on='key', how='outer') #取合集

df5 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})
df6 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})
pd.merge(df5, df6, on='key', how='left') #多對多，對齊左邊，rows=笛卡爾積(Cartesian product)
pd.merge(df5, df6, on='key', how='inner') #會少了c而已

dfl = DataFrame({'key1': ['foo', 'foo', 'bar'],
                 'key2': ['one', 'two', 'one'],
                 'lval': [1, 2, 3]})
dfr = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                 'key2': ['one', 'one', 'one' ,'two'],
                 'rval': [4, 5, 6, 7]})
pd.merge(dfl, dfr, on=['key1', 'key2'], how='outer')

pd.merge(dfl, dfr, on='key1') #相同名字的python會自動更新名字
pd.merge(dfl, dfr, on='key1', suffixes=('_left', '_right')) #用suffixes會更直接與實用

##索引上的合併
dfl1 = DataFrame({'key': ['a' ,'b', 'a', 'a', 'b', 'c'],
                  'value': range(6)})
dfr1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
dfl1
dfr1
pd.merge(dfl1, dfr1, left_on='key', right_index=True) #左邊用key, 右邊用index
pd.merge(dfl1, dfr1, left_on='key', right_index=True, how='outer') #多一row='c'

dflh = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                  'key2': [2000, 2001, 2002, 2001, 2002],
                  'data': np.arange(5.)})
dfrh = DataFrame(np.arange(12).reshape((6, 2)), index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                 [2001, 2000, 2000, 2000, 2001, 2002]], columns=['event1', 'event2'])
dflh
dfrh
pd.merge(dflh, dfrh, left_on=['key1', 'key2'], right_index=True) #要指名用作合併的多個columns
pd.merge(dflh, dfrh, left_on=['key1', 'key2'], right_index=True, how='outer')

dfl2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                 columns=['Ohio', 'Nevada'])
dfr2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13., 14.]], index=list('bcde'),
                 columns=['Missouri', 'Alabama'])
pd.merge(dfl2, dfr2, how='outer', left_index=True, right_index=True)
dfl2.join(dfr2, how='outer') #快速實現索引值合併
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]], index=list('acef'),
                    columns=['New York', 'Oregon'])
dfl2.join([dfr2, another]) #簡單的索引合併可以傳入多組DF，concat函數也可以實現此功能
dfl2.join([dfr2, another], how='outer')

#軸向連接，page195中間有不錯的問題可以思考，page198表7-2有concat函數
s1 = Series([0, 1], index=list('ab'))
s2 = Series([2, 3, 4], index=list('cde'))
s3 = Series([5, 6], index=list('fg'))
pd.concat([s1, s2, s3]) #預設的話就是不重複直接合併成Series
pd.concat([s1, s2, s3], axis=1) #設定axis=1變成DF

s4 = pd.concat([s1*5, s3])
s4
pd.concat([s1, s4], axis=1)
pd.concat([s1, s4], axis=1,join='inner')
pd.concat([s1, s4], axis=1, join_axes=[list('acbe')]) #可以指定新的index
results = pd.concat([s1, s1, s3], keys=['one', 'two', 'three']) #利用keys可以製造層級的DF
results
results.unstack()
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']) #如果axis=1，keys會變成columns name

df7 = DataFrame(np.random.randn(3, 4), columns=list('abcd'))
df8 = DataFrame(np.random.randn(2, 3), columns=list('bda'))
pd.concat([df7, df8], ignore_index=True) #把舊有的index捨棄，直接合併成新的

#合併重疊數據
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=list('fedcba'))
b = Series(np.arange(len(a), dtype=np.float64),
           index=list('fedcba'))
a, b
b[-1] = np.nan

np.where(pd.isnull(a), b, a)
b[:-2].combine_first(a[2:]) #combine_first也可以實現一樣的功能

df7 = DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})
df8 = DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})
df7.combine_first(df8)

#重塑和軸向旋轉
##重塑層次化索引
df9 = DataFrame(np.arange(6).reshape((2, 3)), 
                index=pd.Index(['Ohio', 'Colorado'], name='state'),
                columns=pd.Index(['one', 'two', 'three'], name='number'))
df9
result9 = df9.stack() 
result9 #stack將數據的列旋轉成行
result9.unstack() #unstack重新把數據轉回DF

s1 = Series([0, 1, 2, 3], index=list('abcd'))
s2 = Series([4, 5, 6], index=list('cde'))
df10 = pd.concat([s1, s2], keys=['one', 'two'])
df10.unstack() #會置入NAN值
df10.unstack().stack() #可逆，過濾缺失數據
df10.unstack().stack(dropna=False) #也可以補齊缺漏值

df11 = DataFrame({'left': result9, 'right': result9 + 5},
                 columns=pd.Index(['left', 'right'], name='side'))
df11 #原本的columns=number變成第二層index
df11.unstack('state') #將state變成columns
df11.unstack('state').stack('side') #講side跟state交換

##將長格式旋轉成寬格式
"""先處理資料
raw_macrodata = pd.read_csv('macrodata.csv')
period = pd.PeriodIndex(year=raw_macrodata.year, quarter=raw_macrodata.quarter, name='date') #把year+quarter變成index
used_data = pd.DataFrame(raw_macrodata.to_records(), columns=pd.Index(['realgdp', 'infl', 'unemp'], name='item'),
                         index=period.to_timestamp('D', 'end')) #1. to_records()必須要有，不然會nan 2.to_timestamp需要再看
long_data = used_data.stack().reset_index().rename(columns={0:'value'}) # 1. reset_index => 讓index變成columns/date就有新值 2.rename()需要再看
long_data.to_csv('macrodata_long.csv') #傳回去csv就完成了

ldata = pd.read_csv('macrodata_long.csv')
ldata = ldata.drop(['Unnamed: 0'], axis=1) #回傳多一行，需要找方法處理這個問題"""

ldata = pd.read_csv('macrodata_long.csv')
ldata[:10]
pivoted = ldata.pivot('date', 'item', 'value') 
pivoted.head() #ldata.unstack()沒有辦法unstack因為沒有層次，stack的會變成series的格式儲存

ldata['value2'] = np.random.randn(len(ldata))
ldata.head()
pivoted1 = ldata.pivot('date', 'item')
pivoted1.head() #忽略最後一個值會得到帶有層次化的DF
pivoted1['value'][:5]

unstacked = ldata.set_index(['date', 'item']).unstack('item')
unstacked.head() #pivot是個快捷方式，可以用set_index在unstack達成一樣的效果

#數據轉換
##移除重複數據
df12 = DataFrame({'k1': ['one']*3 + ['two']*4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
df12
df12.duplicated() #返回布林行Series，True代表重複
df12.drop_duplicates() #移除重複值，但是index不變 => #df12.drop_duplicates().reset_index().drop('index', axis=1)

df12['v2'] = range(7)
df12.drop_duplicates(['k1']) #可以指定要移除哪一列的重複值

df12.drop_duplicates(['k1', 'k2'], keep='last') #保留重複的最後一個，default是保留遇到的第一個

##利用函數或映射進行數據轉換
df13 = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'honey ham',
                  'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
df13
meat_to_animal = {
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow',
        'corned beef': 'cow',
        'honey ham': 'pig',
        'nova lox': 'salmon'
}
df13['animal'] = df13['food'].map(str.lower).map(meat_to_animal) #map可以放函數，或是字典
df13['food'].map(lambda x: meat_to_animal[x.lower()]) #可以利用lambda處理

##替換值
s1 = Series([1., -999., 2., -999., -1000., 3.])
s1.replace(-999, np.nan) #可以用map，但是利用replace更快
s1.replace([-999, -1000], np.nan)
s1.replace([-999, -1000], [np.nan, 0]) #用list
s1.replace({-999: np.nan, -1000: 0}) #用dict

##重命名軸索引
df14 = DataFrame(np.arange(12).reshape((3, 4)),
                 index=['Ohio', 'Colorado', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
df14.index.map(str.upper)
df14.index = df14.index.map(str.upper)
df14 #把值丟給index，用map

df14.rename(index=str.title, columns=str.upper) #只能轉換大小寫
df14.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'peekaboo'}) #利用字典可以轉換又不改變內容
_ = df14.rename(index={'OHIO': 'INDIANA'}, inplace=True)
df14 #inplace=True讓可以再指派物件，可以就地修改數據

##離散化和面元(bin)劃分
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100] #範圍為18-25 / 26-35 / 36-60 / 61-100
cats = pd.cut(ages, bins) 
cats #(18, 25] => 大於18，25以下
cats.codes #表示不同分類名稱的label屬性
cats.levels
pd.value_counts(cats) #返回區間的計數
pd.cut(ages, bins, right=False) # [18, 25) => 相反變成18以上，小於25
group_names = ['Youth', 'YouthAdult', 'MiddleAge', 'Senior']
cats_1 = pd.cut(ages, bins, labels=group_names)
pd.value_counts(cats_1) #計數名稱就變成groupnames

data = np.random.rand(20)
data 
cats_2 = pd.cut(data, 4, precision=2) #因為不是準確設定分界，但是可以設定要分幾組，然後precision設定小數位，自動平均分配
cats_2.value_counts()

cats_2_1 = pd.qcut(data, 4)
cats_2_1.value_counts() #比起cut，qcut可以讓數值平均在各個組別內，qcut也可以自訂分組的間距

##檢測和過濾極端值(outlier)
np.random.seed(12345)
df15 = DataFrame(np.random.randn(1000, 4))
df15.describe()
col = df15[3]
col[np.abs(col) > 3] #找出絕對值大於3的數
df15[(np.abs(df15) > 3).any(1)] #找出有任一有大於3的rows，any(1) => axis=1
df15[np.abs(df15) > 3] = np.sign(df15) * 3 #np.sign是返回-1和1組成的array
df15.describe() #能看出來max=3 / min=-3

##排列和隨機抽樣
df16 = DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(len(df16.index))
sampler #產生一個隨機排列的array
df16
df16.take(sampler) #對index重新排列
df16.take(sampler[:3]) #可以在此選擇子集

##計算指標與Dummy 
df17 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                  'data1': range(6)})
pd.get_dummies(df17['key'])
dummies = pd.get_dummies(df17['key'], prefix='key')
df17_dum = df17[['data1']].join(dummies)
df17_dum

###建立指標的方式，但是對於大規模的數據庫時，會變得很慢，需要改良
mnames = ['movie_id', 'tittle', 'genres']
movies = pd.read_table('/Users/changyueh/Desktop/CodePractice/Data_Analysis/Chapt2/ml-1m/movies.dat', sep='::',
                       header=None, names=mnames)
movies[:10]
genre_iter = (set(x.split('|')) for x in movies.genres) #迭代每一個genre
genres = sorted(set.union(*genre_iter)) #列出所有的genre，經過去重
dummies = DataFrame(np.zeros((len(movies.index), len(genres))), columns=genres) #建構全是零，columns=genres數目的DF
for i, gen in enumerate(movies.genres):
    dummies.loc[i, gen.split('|')] = 1 #說明寫在page216
dummies.head()
movies_windic = movies.join(dummies.add_prefix('Genre_')) #直接用join，並且增加columns的前綴
movies_windic.iloc[0]

values = np.random.rand(10)
values
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
ranks = ['0<x<=0.2', '0.2<x<=0.4', '0.4<x<=0.6', '0.6<x<=0.8', '0.8<x<=1.']
pd.get_dummies(pd.cut(values, bins, labels=ranks))

#字符串操作
##字符串對象方法，p218表7-3有所有的內置字符串方式
val = 'a,b, guido'
val.split(',') #內置的split可以做很多事

pieces = [x.strip() for x in val.split(',')]
pieces #strip會自動把空白取消

first, second, third = pieces
first + '::' + second + '::' + third #利用加法可以重新用不同分好連接起來
'::'.join(pieces) #利用join是更實用的方法

'guido' in val #利用in查詢
val.index(',') #index可以查詢定位
val.find(':') #沒有就返回-1，如果用index查詢就會報錯，所以用find比較好

val.count(',') 
val.replace(',', '::') #要是str才能做
val.replace(',', '')           

#正則表達式regex
import re
text = 'foo  bar\t baz  \tqux'
re.split('\s+', text) #\s+ 描述一個或多個空白符

regex = re.compile('\s+') #編輯一個可以重複使用的對象，如果要對許多字符應用，最好的是這個方法
regex.split(text) #使用\s+的正則表達式
regex.findall(text) #找出匹配regex的所有模式，有空白、跟\t

text1 = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE) #re.IGNORECASE讓正則表達式對大小寫不敏感
regex.findall(text1) #因為pattern所以返回郵箱

m = regex.search(text1)
m #返回起始處，跟結束處
text1[m.start():m.end()] #也是一個list找出來5:20

print(regex.match(text1)) #返回None因為只匹配出現在字符串開頭的模式？ => 還需要再解釋

print(regex.sub('REDACTED', text1)) #找出匹配的模式然後替換成指定字符

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})' #如果想要找出email的分段，只需要再加上括號
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match('wesm@bright.net')
m.groups() #返回由模式各段組成的tuple
regex.findall(text1) #返回有數個tuple的list
print (regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text1)) #利用\1等特殊符號訪問個匹配項目的分組

regex = re.compile(r"""
        (?P<username>[A-Z0-9._%+-]+)
        @
        (?P<domain>[A-Z0-9.-]+)
        \.
        (?P<suffix>[A-Z]{2,4})""", flags=re.IGNORECASE|re.VERBOSE) #可以讓匹配項目得到一個簡單的分組的字典
m = regex.match('wesm@bright.net')
m.groupdict() #返回字典

##pandas中向量的字符串函數
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com', 
        'Rob': 'rob@fmail.com', 'Wes': np.nan}
data = Series(data)
data
data.isnull()
data.str.contains('gmail') #忽視NA值去訪問，令其不會報錯
pattern
data.str.findall(pattern, flags=re.IGNORECASE) #也可以使用正則表達式

matches = data.str.match(pattern, flags=re.IGNORECASE) #以下的都不能操作，要再查看
#matches
#matches.str.get(1)
#matches.str[0]

data.str[:5]

#USDA食品數據庫