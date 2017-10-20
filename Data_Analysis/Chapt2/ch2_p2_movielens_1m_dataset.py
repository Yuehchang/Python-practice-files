#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:03:41 2017

@author: changyueh
"""

"""
Dataset from http://www.groupbylens.org/node/73
"""
import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip'] #查看users.dat發現沒有表頭，所以幫忙製造

users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']

ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']

movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=mnames)

#切片語法查看是否導入順利
users[:5]
ratings[:5]
movies[:5]

#merge three tables
data = pd.merge(pd.merge(ratings, users), movies) #會由表頭判別，由結果來看還滿準

data.ix[0] ###但是合併顯示出的結果跟文章不同，這點可以去討論！

#使用pivot_table
mean_ratings_gender = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
                                            
#去除評分數不到250的電影評分
"""
步驟為： 
1. 製作出利用電影名稱所計數的Series
2. 利用Series篩選出沒有大於該條件的index
3. 回到原本的table利用新建立的index去篩選出想要的新table
"""
rating_by_title = data.groupby('title').size() #利用size製作成一個Series
rating_by_title[:10]

active_titles = rating_by_title.index[rating_by_title >= 250] #找出大於250的index

mean_ratings_over250 = mean_ratings_gender.ix[active_titles] #篩選條件變成active_title(唯有條件的index)

top_female_ratings = mean_ratings_over250.sort_index(by='F', ascending=False) #對女性做排列，只有女生的會排，男生的不動

#計算評分差異
#1. 計算男女之間的差，然後對其排列
mean_ratings_over250['diff'] = mean_ratings_over250['M'] - mean_ratings_over250['F']                                                    
sort_by_diff = mean_ratings_over250.sort_index(by='diff')  
sort_by_diff[:10] #因為是男減女所以負數是女生最愛
sort_by_diff[::-1][:10] #利用從最後面開始數，得出男生最愛                                                

#2. 不限性別的差異
#根據電影名稱的標準差
rating_std_by_title = data.groupby('title')['rating'].std()
#根據active_title進行過濾
rating_std_by_title = rating_std_by_title.ix[active_titles]
#根據Series進行排序
rating_std_by_title.order(ascending=False)[:10] #是Series所以沒有sort_index

                                                    
                                                    