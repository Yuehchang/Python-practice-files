#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:22:00 2017

@author: changyueh
"""
import numpy as np
import pandas as pd

#matplotlib API入門
import matplotlib.pyplot as plt

##Figure and Subplot，page235表8-1
fig = plt.figure() #圖像都存在figure中，但不能通過空figure繪圖，需要窗建一個subplot
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3) #前兩個是2x2的圖像，第三個是順序

from numpy.random import randn
plt.plot(randn(50).cumsum(), 'k--') #沒有指定，就直接畫在最後一個

_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3) #長條圖
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30)) #散步圖，但是止於二維，也不用指派

fig, axes = plt.subplots(2, 3)
axes #因為fig跟subplots太常見，可以利用上述的簡單方法創建一個新的fig跟返回一個含有已創建的subplot對象的NumPy

##調整subplot之間的間距
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True) #座標分享
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0) #消除間距

##顏色、標記、和線型
fig, axes = plt.subplots(1, 1)
plt.plot(randn(30).cumsum(), 'ko--')
plt.plot(randn(30).cumsum(), color='k', linestyle='dashed', marker='^') #更明確的格式

data = randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='step-post')
plt.legend(loc='best') #一樣的數據點，但可以利用drawstyle修改線性的圖

##刻度、標籤、與圖例(legend)
fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages') #y的修改方法也一樣，只要依序把x_改為y_

fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(1000).cumsum(), 'k', label='one') #可以利用label來新增legend
ax.plot(randn(1000).cumsum(), 'r--', label='two')
ax.plot(randn(1000).cumsum(), 'b.', label='three')
ax.plot(randn(1000).cumsum(), 'y', label='_nolegend_') #利用_nolegend_可以單個不展示
ax.legend(loc='best') #最後需要這條指令把label展現出來，best可以自動最優的選擇擺放位置

#註解與在Subplot上面繪圖
##註解，在matplotlib庫中有更多註解的解釋
from datetime import datetime
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

data = pd.read_csv('spx.csv', index_col=0, parse_dates=True)
spx = data['SPX']

spx.plot(ax=ax, style='k-')

crisis_data = [
        (datetime(2007, 10, 11), 'Peak of bull market'),
        (datetime(2008, 3, 12), 'Bear Stearns Fails'),
        (datetime(2008, 9, 15), 'Lehman Bankruptcy')]

for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 50),
                xytext=(date, spx.asof(date) + 200),
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left', verticalalignment='top')

ax.set_xlim(['1/1/2007', '1/1/2011']) #放大到2007-2010
ax.set_ylim([600, 1800])

ax.set_title('Important dates in 2008-2009 financial crisis')

##繪圖
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)

ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon) #繪圖時添加的需要依靠這個指令

#將圖表保存到文件，page244表8-2有save的參數
plt.savefig('figpath.svg') #svg file

plt.savefig('figpath.png', dpi=400, bbox_inches='tight') #png file

#matplotlib的配置，page244，使用plt.rc，參數最好傳入字典

#pandas中的繪圖函數
##線性圖，page246-267表8-3/8-4有Series & DataFrame的plot函數
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
plt.savefig('linegraph.png', dpi=400, bbox_inches='tight') #不能用s.savefig / 要用plt.savefig，預設前一個圖

df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
                  columns=list('ABCD'),
                  index=np.arange(0, 100, 10))
df.plot() #自動畫出四條線，並加上legend

##柱狀圖
fig, axes = plt.subplots(2, 1) #兩行，一列
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
data.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)

df = pd.DataFrame(np.random.rand(6, 4),
               index=['one', 'two', 'three', 'four', 'five', 'six'],
               columns=pd.Index(list('ABCD'), name='Genus'))
df.plot(kind='bar')
df.plot(kind='barh', stacked=True, alpha=0.5) #堆疊

###小費練習題
path = '/Users/changyueh/Desktop/CodePractice/Data_Analysis/Chapt9/tips.csv'
tips = pd.read_csv(path)
party_counts = pd.crosstab(tips.day, tips.size) #這步用不下去

##直方圖和密度圖
tips['tip_pct'] = (tips.tip / (tips.total_bill + tips.tip)).round(2)
tips.tip_pct.hist(bins=50)
tips.tip_pct.plot(kind='kde') #KDE = Kernel Density Estimate 核密度估計，計算密度圖

###雙峰分佈練習圖
comp1 = np.random.normal(0, 1, size=200) #N(0, 1)
comp2 = np.random.normal(10, 2, size=200) #Second parameter = standard deviatoin / N(10, 4) 
value = pd.Series(np.concatenate([comp1, comp2]))
value.hist(bins=100, alpha=0.3, color='k', normed=True)
value.plot(kind='kde', style='k--')

##散布圖
path_macro = '/Users/changyueh/Desktop/CodePractice/Data_Analysis/Chapt7/macrodata.csv'
macro = pd.read_csv(path_macro)
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
#trans_data_prepare = np.log(data).dropna() #原始的每一個array先取log
trans_data = np.log(data).diff().dropna() #diff(n=1) => 計算first_diff，n=1是default
trans_data[-5:]
plt.scatter(trans_data['m1'], trans_data['unemp'])
plt.title('Changes in log %s vs. log %s' % ('m1', 'umemp'))
pd.scatter_matrix(trans_data, diagonal='kde', color='k', alpha=0.3) #很好用的圖，對角線可以放上直方圖or密度圖

##地圖
path_haiti = '/Users/changyueh/Desktop/CodePractice/Data_Analysis/Chapt8/Haiti.csv'
data = pd.read_csv(path_haiti)

###step1 檢查數據
data[['INCIDENT DATE', 'LATITUDE', 'LONGITUDE']][:10] #每一筆資料都有時間與位置
data['CATEGORY'][:6] #每一筆數值都是由逗點分隔的代碼
data.describe() #發現地理位置有偏移許多的數據
data = data[(data.LATITUDE > 18) & (data.LATITUDE <20) &
            (data.LONGITUDE > -75) & (data.LONGITUDE < -70) &
            data.CATEGORY.notnull()]
data.describe()

###step2 數據做規整化，拆分與法語轉英語
def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(',')) #strip() => 'http://python-reference.readthedocs.io/en/latest/docs/str/strip.html'
    return [x for x in stripped if x] #變成返回成list但是要x為True

def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets)) #union => make it distinct 

def get_english(cat):
    code, names = cat.split('.') #從.開始分離，code=數值 / names=法文跟英文
    if '|' in names:
        names = names.split('|')[1] #取後面是英文的部分
    return code, names.strip()

###step3 檢查寫的函式
get_english('2. Urgences logistiques | Vital Lines')

###step4 製作編碼跟名稱映射的字典
all_cats = get_all_categories(data.CATEGORY)
english_mapping = dict(get_english(x) for x in all_cats) #生成器表達式
english_mapping['2a']
english_mapping['6c']

###step5 製造dummies
def get_code(seq):
    return [x.split('.')[0] for x in seq if x]
all_codes = get_code(all_cats)
code_index = pd.Index(np.unique(all_codes))
dummy_frame = pd.DataFrame(np.zeros((len(data), len(code_index))), index=data.index,
                        columns=code_index)

###step6 將1值填入
for row, cat in zip(data.index, data.CATEGORY):
    code = get_code(to_cat_list(cat))
    dummy_frame.loc[row, code] = 1 

###step7 Join
data = data.join(dummy_frame.add_prefix('category_'))

###step8 plot to map
from mpl_toolkits.basemap import Basemap #matplotlib.github.com/basemap

def basic_haiti_map(ax=None, lllat=17.25, urlat=20.25,
                    lllon=-75, urlon=-71):
    #創建球面投影的Basemap
    m = Basemap(ax=ax, projection='stere',
                lon_O=(urlon + lllon) / 2,
                lat_O=(urlat + lllat) / 2,
                llcrnrlat=lllat, urcrnrlat=urlat,
                llcrnrlon=lllon, urcrnrlon=urlon,
                resolution='f')
    m.drowcostlines()
    m.drawstates()
    m.drawcountries()
    return m

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
fig.subplots_adjust(hspace=0.05, wspace=0.05)

to_plot = ['2a', '1', '3c', '7a']

lllat=17.25; urlat=20.25; lllon=-75; urlon=-71

for code, ax in zip(to_plot, axes.flat):
    m = basic_haiti_map(ax, lllat=lllat, urlat=urlat,
                        lllon=lllon, urlon=urlon)
    cat_data = data[data['category_{}'.format(code)] == 1]
    
    #計算地圖的投影座標
    x, y = m(cat_data.LONGITUDE, cat_data.LATITUDE)
    
    m.plot(x, y, 'k.', alpha=0.5)
    ax.set_title('{0}: {1}'.format(code, english_mapping[code])) ##Basemap沒有辦法使用，還要再用一次
