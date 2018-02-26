#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:52:54 2018

@author: changyueh
"""

#Nonlinear relationships using random forests
exec(open('./chapt10/0_data.py').read())

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

X = df[['LSTAT']].values
y = df['MEDV'].values

tree = DecisionTreeRegressor(max_depth=5)
tree.fit(X, y)

sort_idx = X.flatten().argsort()
lin_regplot(X[sort_idx], y[sort_idx], tree)
plt.xlabel('% lower status of the population [LSTAT]')
plt.ylabel('Price in $1000\'s [MSDV]')
plt.show()

#Random forest regression
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                    random_state=1)

forest = RandomForestRegressor(n_estimators=1000, criterion='mse',
                               random_state=1, n_jobs=-1)
forest.fit(X_train, y_train)
y_train_pred = forest.predict(X_train)
y_test_pred = forest.predict(X_test)

print('MSE train: {0:.3f}, test: {1:.3f}'.format(mean_squared_error(y_train, y_train_pred),
                                                 mean_squared_error(y_test, y_test_pred)))
print('R^2 train: {0:.3f}, test: {1:.3f}'.format(r2_score(y_train, y_train_pred),
                                                 r2_score(y_test, y_test_pred)))
f_importance = forest.feature_importances_
