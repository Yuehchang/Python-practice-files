#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:43:26 2017

@author: changyueh
"""
from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, classifier, resolution=0.02):
    
    #setup marker generator and color map
    markers = ('s','x', 'o', '^', 'v')
    colors = ('red','blue', 'black')
    colors2 = ('green', 'white','yellow')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    cmap2 = ListedColormap(colors2[:len(np.unique(y))])
    
    #plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1 
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpah=0.4, cmap=cmap2)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    #plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[ y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)

##########
import pandas as pd
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)

from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split

X, y = df_wine.ix[:, 1:].values, df_wine.ix[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

"""
Computing the scatter matrices page 140
"""
import numpy as np
np.set_printoptions(precision=4)
mean_vecs = []
for label in range(1,4):
    mean_vecs.append(np.mean(X_train_std[y_train==label], axis=0))
    print('MV %s: %s\n' %(label, mean_vecs[label-1]))
    
"""
Within-class scatter matrix page 141
by summing up the individual scatter matrices Si of each individual class i
"""
d = 13 #number of features
S_W = np.zeros((d,d))
for label, mv in zip(range(1,4), mean_vecs):
    class_scatter = np.zeros((d,d))
    for row in X_train[y_train==label]:
        row, mv = row.reshape(d, 1), mv.reshape(d, 1)
        class_scatter += np.dot((row - mv), (row - mv).T)
    S_W += class_scatter
print ('Within-class scatter matrix: %sx%s' % (S_W.shape[0], S_W.shape[1]))

#scale the matrices to normalized version
d = 13
S_W = np.zeros((d,d))
for label, mv in zip(range(1,4), mean_vecs):
    class_scatter = np.cov(X_train_std[y_train==label].T)
    S_W += class_scatter
print('Scaled within-class scatter matrix: %sx%s' % (S_W.shape[0], S_W.shape[1]))

"""
Between-class scatter matrix page 142
mi-m
"""
mean_overall = np.mean(X_train_std, axis=0)
d = 13 
S_B = np.zeros((d,d))
for i, mean_vec in enumerate(mean_vecs):
    n = X_train[y_train==i+1, :].shape[0]
    mean_vec = mean_vec.reshape(d,1)
    mean_overall = mean_overall.reshape(d,1)
S_B += n * np.dot((mean_vec - mean_overall), (mean_vec - mean_overall).T)
print('Between-class scatter matrix: %sx%s' % (S_B.shape[0], S_B.shape[1]))

#Selecting linear discriminants for the new feature subspace
eigen_vals, eigen_vecs = np.linalg.eig(np.dot(np.linalg.inv(S_W), S_B))

eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:,i]) for i in range(len(eigen_vals))]
eigen_pairs = sorted(eigen_pairs, key = lambda k: k[0], reverse=True)
print('Eigenvalues in decreasing order: \n')
for eigen_val in eigen_pairs:
    print(eigen_val[0])
    
#stacking two most dicriminative eigenvector columns
w = np.hstack((eigen_pairs[0][1][:, np.newaxis].real, eigen_pairs[1][1][:, np.newaxis].real))
print ('Matrix W:\n', w)

#projecting smaples onto the new feature space X' = XW
from matplotlib import pyplot as plt
X_train_lda = X_train_std.dot(w)
colors = ['r','b','g']
markers = ['s','x','o']
for l, c, m in zip(np.unique(y_train), colors, markers):
    plt.scatter(X_train_lda[y_train==l, 0]*(-1), X_train_lda[y_train==l, 1]*(-1), c=c, label=l, marker=m)
plt.xlabel('LD 1')
plt.ylable('LD 2')
plt.legend(loc='lower right')
plt.show

"""
LDA via scikit-learn page 146
"""
from sklearn.lda import LDA
from sklearn.linear_model import LogisticRegression

lda = LDA(n_components=2)
X_train_lda = lda.fit_transform(X_train_std, y_train)

lr = LogisticRegression()
lr = lr.fit(X_train_lda, y_train)
plot_decision_regions(X_train_lda, y_train, classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.legend(loc='lower left')
plt.show()

X_test_lda = lda.transform(X_test_std)
plot_decision_regions(X_test_lda, y_test, classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.legend(loc='lower left')
plt.show()

#extra thing to findout 
from sklearn.metrics import accuracy_score
y_pred = lr.predict(X_train_lda)
y_pred1 = lr.predict(X_test_lda)
print('Accuracy for training data: %.2f' % accuracy_score(y_train, y_pred))
print('Accuracy for test data: %.2f' % accuracy_score(y_test, y_pred1))