#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:40:40 2017

@author: changyueh
"""

"""
Simple Linear regression model
"""
exec(open('./chapt10/0_data.py').read())

#EDA
#1. scatterplot matrix
import matplotlib.pyplot as plt
import seaborn as sns #standford.edu/~mwaskom/software/seaborn/

sns.set(style='whitegrid', context='notebook')
cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
sns.pairplot(df[cols], size=2.5) #pairplot = scatterplot
plt.show()

#2. correlation matrix
import numpy as np
cm = np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.5)
hm = sns.heatmap(cm, cbar=True, annot=True,
                 square=True, fmt='.2f',
                 annot_kws={'size': 15},
                 yticklabels=cols, xticklabels=cols)#heatmap = heatmap
plt.show()

#ordinary least squares linear regression model(OLS)
#GD implementation of Adaline page285
class LinearRegressionGD(object):
    
    def __init__(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return self.net_input(X)        

X = df[['RM']].values
y = df['MEDV'].values
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
X_std = sc_x.fit_transform(X)
y_std = sc_y.fit_transform(y)
lr = LinearRegressionGD()
lr.fit(X_std, y_std)

plt.plot(range(1, lr.n_iter+1), lr.cost_)
plt.ylabel('SSE')
plt.xlabel('Epoch')
plt.show() #GD algorithm coverged after the fifth epoch

#visualize linear regression fits the training data
def lin_regplot(X, y, model):
    plt.scatter(X, y, c='blue')
    plt.plot(X, model.predict(X), color='red')
    return None

lin_regplot(X_std, y_std, lr)
plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000\'s [MEDV]')
plt.show()

#inverse the StandardScaler
num_rooms_std = sc_x.transform([5.0])
price_std = lr.predict(num_rooms_std)
print('Price in $1000\'s: %.3f' % (sc_y.inverse_transform(price_std)))



                 