#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:24:36 2017

@author: changyueh
"""

"""
Dataset from http://www.ssa.gov/oact/babynames/limits.html?
"""

#利用UNIX的命令式察看其中一個文件的前10行
#!head -n 10 names/yob1880.txt

import pandas as pd
import numpy as np

names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
names1880

#利用出生年的性別分處來總計該年的出生數
names1880.groupby('sex').births.sum()

#將所有年份放入一個DataFrame，並新增一個year欄位，使用pandas.concat
years = range(1880, 2011) #從1880到2010年，所以要多一個

pieces = [] #先創建一個空list
columns = ['name', 'sex', 'births']

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns) #最後在variable只會展現最後一個值的年份
    
    frame['year'] = year #創立year欄位
    pieces.append(frame) #變成list，每一個row中都包含每個年份的dataframe
    
names_total = pd.concat(pieces, ignore_index=True) #將pieces展開成完整的DataFrame

#對其年級與性別製作pivot_table
births_of_sex_year = names_total.pivot_table('births', index='year', columns='sex', aggfunc=sum)
births_of_sex_year.tail()

births_of_sex_year.plot(title='Total births by sex and year')

#插入名字的佔比數
def add_prop(group):
    births = group.births.astype(float)
    
    group['prop'] = births / births.sum()
    
    return group

names_total_with_prop = names_total.groupby(['year', 'sex']).apply(add_prop)

np.allclose(names_total_with_prop.groupby(['year', 'sex']).prop.sum(), 1) #利用np.allclose來檢查是否總和為1

def get_top1000(group): #找出前一千名的子集合
    return group.sort_index(by='births', ascending=False)[:1000]

grouped = names_total_with_prop.groupby(['year', 'sex'])
#不能使用top1000 = grouped.apply(grouped.sort_index(by='births', ascending=False)[:1000])
top1000 = grouped.apply(get_top1000)

#未完待續...先到後幾章研究