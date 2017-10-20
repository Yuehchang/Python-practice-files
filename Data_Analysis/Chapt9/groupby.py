#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:40:46 2017

@author: changyueh
"""
#GroupBy
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                'key2': ['one', 'two', 'one', 'two', 'one'],
                'data1': np.random.randn(5),
                'data2': np.random.randn(5)})
df
grouped = df['data1'].groupby(df['key1']) 
grouped #grouped只是一個groupby的對象，並沒有進行任何運算
grouped.mean() #需要應用方法才可以達成，並產生了新的Series"key1"，會叫key1因為聚合的columns的名字就是key1

means = df['data1'].groupby([df['key1'], df['key2']]).mean() #groupby要聚合兩個columns，裡面要放list
means #r具有層次的Series
means.unstack() #變成DF

states = np.array(['Ohio', 'Califorina', 'Califorina', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006]) 
df['data1'].groupby([states, years]).mean() #除了Series也可以利用長度適當的narray

df.groupby('key1').mean() #可以直接用列名，計算所有的聚合
df.groupby(['key1', 'key2']).mean() #在上述的會自動捨棄key2因為不是數值

df.groupby(['key1', 'key2']).size() #返回各組的分組數

##對分組進行迭代
for name, group in df.groupby('key1'):
    print(name) #name=在key1裡面的分組值
    print(group) #返回其所有的值

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print(k1, k2)
    print(group) #多重的話元祖的第一個元素是由鍵值組成的元組
    
pieces = dict(list(df.groupby('key1'))) #如果沒有list裡面的都是str，無法dict
pieces['b']

df.dtypes
grouped = df.groupby(df.dtypes, axis=1)
dict(list(grouped)) #變成都是float64的一組，object的一組

##選取一個或一組列
r1 = df['data2'].groupby([df['key1'], df['key2']]).mean()
type(r1) #返回一個Series
r2 = df.groupby(['key1', 'key2'])[['data2']].mean()
type(r2) #返回一個DF
r3 = df.groupby(['key1', 'key2'])['data2'].mean()
type(r3) #[]返回Series跟r1一樣，[[]]返回DF

##通過字典或Series進行分組
people = DataFrame(np.random.randn(5, 5),
                   columns=list('abcde'),
                   index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.loc[2:3, ['b', 'c']] = np.nan
people
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}
by_column = people.groupby(mapping, axis=1) #利用字典去分組
by_column.sum() #把columns指派給不同分組，然後整合在一起
map_series = Series(mapping)
map_series
people.groupby(map_series, axis=1).count() #代表可以用series分組

##通過函數進行分組
people.groupby(len).sum() #想要利用不同名字的字母數來分類，其實利用len就可以

key_list = ['one', 'one', 'one', 'two', 'two']
r4 = people.groupby([len, key_list]).min() #沒有axis=1就都是對index處理
type(r4)

##根據索引級別分組
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                     [1, 3, 5, 1, 3]], names=['city', 'tenor'])
hier_df = DataFrame(np.random.randn(4, 5), columns=columns)
hier_df
hier_df.groupby(level='city', axis=1).count() #使用level來分組

##數據聚合，page273表9-1有經過優化的groupby方法
df #13rows命名過了
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9) #再看一次

def peak_to_peak(arr):
    return arr.max() - arr.min()
grouped.agg(peak_to_peak) #利用agg()的函數可以在裡面放入自定義的函數
grouped.describe() #類似聚合的自帶功能，但是準確來說不是

##面向列的多函數應用，高級聚合功能
tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips.head()

grouped = tips.groupby(['sex', 'smoker'])
grouped_pct=grouped['tip_pct']
grouped_pct.mean() #grouped_pct.agg('mean') 可以使用字符串形式使用函數
grouped_pct.agg(['mean', 'std', peak_to_peak]) #使用agg可以一次apply多個函數，返回的columns是函數的名字
grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]) #可以直接命名，利用一個list多個tuple

functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
result #利用functions產生的list直接應用
result['tip_pct'] #result.iloc[:, 0:3]

ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
grouped['tip_pct', 'total_bill'].agg(ftuples) #也可以傳入自定義的tuple

grouped.agg({'tip': np.max, 'size': 'sum'}) #對不同的columns應用不同的函數，利用字典
grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'], 
             'size': 'sum'}) #只有在多個函數應用到至少一個columns時，DF才會擁有層次化的columns

##以"無索引"的形式返回聚合數據
tips.groupby(['sex', 'smoker'], as_index=False).mean()

#分組及運算和轉換
df #13row命名過了
k1_means = df.groupby('key1').mean().add_prefix('mean_')
k1_means #DF
pd.merge(df, k1_means, left_on='key1', right_index=True) #先聚合找出mean，然後再合併數據

key = ['one', 'two', 'one', 'two', 'one']
people.groupby(key).mean()
people.groupby(key).transform(np.mean) #直接在數據中轉換，但是要想好groupby的函數
#people.groupby(len).transform(np.mean)

def demean(arr):
    return arr - arr.mean()
demeaned = people.groupby(key).transform(demean)
demeaned #NaN被排除
demeaned.groupby(key).mean().round() #可以看到被很好的利用

##apply: 一般性的“拆分-應用-合併”
def top(df, n=5, columns='tip_pct'):
    return df.sort_values(by=columns, ascending=False)[:n]
top(tips, n=5)
tips.groupby('smoker').apply(top)
tips.groupby(['smoker', 'day']).apply(top, n=1, columns='total_bill')

tips.groupby(['smoker', 'day'])['tip_pct'].describe() #隨然tip_pct只用一個[]但還是DF，因為describe返回的就是DF

##禁止分組鍵
tips.groupby('smoker', group_keys=False).apply(top)

##分位數quantile和桶bucket分析
frame = DataFrame({'data1': np.random.randn(1000),
                   'data2': np.random.randn(1000)})
factor = pd.cut(frame.data1, 4) #分布不均的組
factor[:10]

def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}
frame.groupby(factor)['data2'].apply(get_stats).unstack() #frame['data2'].groupby(factor).apply(get_stats).unstack()一樣

grouping = pd.qcut(frame.data1, 10, labels=False)
frame['data2'].groupby(grouping).apply(get_stats).unstack() #用grouping可以得到平均分配的組

###範例：用於特定分組的值填充缺失值
s = Series(np.random.randn(6))
s[::2] = np.nan
s
s.fillna(s.mean()) #利用其他三個的平均去填充

states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East']*4 + ['West']*4
data = Series(np.random.randn(8), index=states)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
data
data.groupby(group_key).mean()

fill_mean = lambda g: g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean) #利用分組的平均去填充NA值，data.fillna(data.mean())用全組的去平均

fill_value = {'East': 0.5, 'West':-1}
fill_func = lambda g: g.fillna(fill_value[g.name]) #name屬性如何得知？？？
data.groupby(group_key).apply(fill_func)

##隨機採樣和排列
suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10]*3 ) * 4
base_name = ['A'] + list(range(2,11)) + ['J', 'Q', 'K']
cards = []
for suit in suits:
    cards.extend(str(num) + suit for num in base_name)
desk = Series(card_val, index=cards)

desk[:10]

def draw(deck, n=5): #隨機抽取五張，利用permutation
    return deck.take(np.random.permutation(len(deck))[:n])
draw(desk) #套用公式，隨機抽取

get_suit = lambda card: card[-1] #只取最後一個字母  
desk.groupby(get_suit).apply(draw, n=2) #分組後各阻止抽兩個
desk.groupby(get_suit, group_keys=False).apply(draw, n=2) #取消分組顯示

##分組加權平均數和相關係數
df = DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b','b', 'b'],
                'data': np.random.randn(8), #return normal distribution
                'weights': np.random.rand(8)}) #return random value btw [0,1]
df
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights']) #np.average: geting average with weights
group_wavg = grouped.apply(get_wavg) #得到分組的加權平均
group_wavg.name = 'wavg'
df.join(group_wavg, on='category') #嘗試合併回去

close_px = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0) #股票實例
close_px[-4:]
rets = close_px.pct_change().dropna()
spx_corr = lambda x: x.corrwith(x['SPX']) #專門計算對SPX的相關係數
by_year = rets.groupby(lambda x: x.year) #直接應用Timestamp
by_year.apply(spx_corr)
by_year.apply(lambda g: g['AAPL'].corr(g['MSFT']))

##面向分組的線性迴歸
import statsmodels.api as sm

def regress(data, yvar, xvars): #OLS的公式
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

by_year.apply(regress, 'AAPL', ['SPX']) #在線性中，'SPX'跟['SPX']的差別？

##透視表和交叉表
tips.pivot_table(index=['sex', 'smoker'])
tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'],
                 columns='smoker')
tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'],
                 columns='smoker', margins=True) #多了一個grand total

tips.pivot_table('tip_pct', index=['sex', 'smoker'], columns='day',
                 aggfunc=len, margins=True)

tips.pivot_table('size', index=['time', 'sex', 'smoker'], columns='day',
                 aggfunc='sum', fill_value=0)

pd.crosstab([tips.time, tips.day], tips.smoker, margins=True)

#Exercise 2012聯邦數據庫
fec = pd.read_csv('P00000001-ALL.csv')
fec.head()
fec.count() #return non-value
fec.iloc[123456]

##加入黨派訊息
unique_cands = fec.cand_nm.unique()
list(unique_cands) 
unique_cands[2] #'Obama, Barack'

parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Romney, Mitt': 'Republican',
           'Obama, Barack': 'Democrat',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'Paul, Ron': 'Republican',
           'Santorum, Rick': 'Republican',
           'Gingrich, Newt': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Perry, Rick': 'Republican'}

fec.cand_nm[123456:123461] #映射候選人名
fec.cand_nm[123456:123461].map(parties) #使用map()返回黨派訊息
fec['party'] = fec.cand_nm.map(parties) #使用map添加訊息
fec['party'].value_counts()

(fec.contb_receipt_amt > 0).value_counts() #返回True/False的counts
fec = fec[fec.contb_receipt_amt > 0] #保留正的出資額
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])] #主要兩個候選人

##根據職業和雇主的統計贊助訊息
fec.contbr_occupation.value_counts()[:10]
occ_mapping = {
        'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
        'INFORMATION REQUESTED': 'NOT PROVIDED',
        'INFORMATION REQUESTED (BEST EFFORTS)': 'NOT PROVIDED',
        'C.E.O': 'CEO'}
f = lambda x: occ_mapping.get(x, x) #dict.get(x, x) 如果沒有x則返回自己
fec.contbr_occupation = fec.contbr_occupation.map(f) #替換occ

emp_mapping = {
        'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
        'INFORMATION REQUESTED': 'NOT PROVIDED',
        'SELF': 'SELF-EMPLOYED',
        'SELF EMPLOYED': 'SELF-EMPLOYED'}
f = lambda x: emp_mapping.get(x, x)
fec.contbr_employer = fec.contbr_employer.map(f)

by_occupation = fec.pivot_table('contb_receipt_amt', index='contbr_occupation',
                                columns='party', aggfunc='sum')
over_2mm = by_occupation[by_occupation.sum(1) > 2000000]
over_2mm.plot(kind='barh')

def get_top_amount(group, key, n):
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.sort_values(ascending=False)[:n]
grouped = fec_mrbo.groupby('cand_nm')
grouped.apply(get_top_amount, 'contbr_occupation', n=7)
grouped.apply(get_top_amount, 'contbr_employer', n=7)

##對出資額分組
bins = np.array([0, 1, 10, 100, 1000, 100000, 1000000, 10000000, 100000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins)
labels
grouped = fec_mrbo.groupby(['cand_nm', labels])
grouped.size().unstack(0) #計算出個數
bucket_sums = grouped.contb_receipt_amt.sum().unstack(0) #算出實際的金額
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1), axis=0) #兩個候選人各區間的比例
normed_sums[:-2].plot(kind='barh', stacked=True)

self_sums = bucket_sums.div(bucket_sums.sum(axis=0), axis=1)
self_sums[:-2].plot(kind='barh', stacked=True)