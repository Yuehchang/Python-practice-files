#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:00:24 2017

@author: changyueh
"""

exec(open('./chapt10/1_linearReg.py').read())

from sklearn.linear_model import LinearRegression
slr = LinearRegression()
slr.fit(X, y)
print('Slope: {:.3f}'.format(slr.coef_[0]))
print('Intercept: {:.3f}'.format(slr.intercept_))

#compare to GD implementation
lin_regplot(X, y, slr)
plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000\'s [MEDV]')
plt.show() #result look the same as GD

#Fitting a robust regression model using RANSAC algorithm
##RANdom SAmple Consensus (a way to throwing out outliers)
from sklearn.linear_model import RANSACRegressor
ransac = RANSACRegressor(LinearRegression(),
                         max_trials=100,
                         min_samples=50,
                         residual_metric=lambda x: np.sum(np.abs(x), axis=1),
                         residual_threshold=5.0,
                         random_state=0)
ransac.fit(X, y) #residual threshold need experience 

##plot the inliers and outliers
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
line_X = np.arange(3, 10, 1)
line_y_ransac = ransac.predict(line_X[:, np.newaxis])
plt.scatter(X[inlier_mask], y[inlier_mask],
            c='blue', marker='o', label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask],
            c='lightgreen', marker='s', label='Outliers')
plt.plot(line_X, line_y_ransac, color='red')
plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000\'s [MEDV]')
plt.legend(loc='upper left')
plt.show()

print('Slope: %.3f' % (ransac.estimator_.coef_[0]))
print('Intercept: {:.3f}'.format(ransac.estimator_.intercept_)) #not sure if this method do well on unseen data

#Evaluating the preformance of linear regrssion models
from sklearn.model_selection import train_test_split
X = df.iloc[:, :-1].values
y = df['MEDV'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
slr = LinearRegression()
slr.fit(X_train, y_train) 
y_train_pred = slr.predict(X_train)
y_test_pred = slr.predict(X_test)

##residual plots => diagnosing regression models 1.detect nonlinearity and outliers 2. errors are randomly distributed
plt.scatter(y_train_pred, y_train_pred - y_train, 
            c='blue', marker='o', label='Training data')
plt.scatter(y_test_pred, y_test_pred - y_test,
            c='lightgreen', marker='s', label='Test data')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=-10, xmax=50, lw=2, color='red')
plt.xlim([-10, 50])
plt.show()

##mean squared error(MSE) / R squared
from sklearn.metrics import mean_squared_error
print('MSE train: {0:.3f}, test: {1:.3f}'.format(
        mean_squared_error(y_train, y_train_pred),
        mean_squared_error(y_test, y_test_pred)))
from sklearn.metrics import r2_score
print('R^2 train: {0:.3f}, test: {1:.3f}'.format(
        r2_score(y_train, y_train_pred),
        r2_score(y_test, y_test_pred)))

#Most popular approaches Ridge Regression / Least Absolute Shrinkage and Selection Operator(LASSO) / Elastic Net 
from sklearn.linear_model import Ridge
ridge = Ridge(alpha=1.0) #alpha is the parameter to regularization strength
ridge.fit(X_train, y_train)
y_train_pred = ridge.predict(X_train)
y_test_pred = ridge.predict(X_test)
print('MSE train: {0:.3f}, test: {1:.3f}'.format(
        mean_squared_error(y_train, y_train_pred),
        mean_squared_error(y_test, y_test_pred)))
print('R^2 train: {0:.3f}, test: {1:.3f}'.format(
        r2_score(y_train, y_train_pred),
        r2_score(y_test, y_test_pred)))

from sklearn.linear_model import Lasso
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)
y_train_pred = lasso.predict(X_train)
y_test_pred = lasso.predict(X_test)
print('MSE train: {0:.3f}, test: {1:.3f}'.format(
        mean_squared_error(y_train, y_train_pred),
        mean_squared_error(y_test, y_test_pred)))
print('R^2 train: {0:.3f}, test: {1:.3f}'.format(
        r2_score(y_train, y_train_pred),
        r2_score(y_test, y_test_pred)))

from sklearn.linear_model import ElasticNet
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5)
elastic.fit(X_train, y_train)
y_train_pred = elastic.predict(X_train)
y_test_pred = elastic.predict(X_test)
print('MSE train: {0:.3f}, test: {1:.3f}'.format(
        mean_squared_error(y_train, y_train_pred)))
print('R^2 train: {0:.3f}, test: {1:.3f}'.format(
        r2_score(y_train, y_train_pred),
        r2_score(y_test, y_test_pred))) 

#more detial in http:\\scikit-learn.org/stable/modules/linear_model.html