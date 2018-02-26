#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:24:45 2017

@author: changyueh
"""

exec(open('./chapt10/2_sklearnReg.py').read())

#polynomial regression
##1. add a second degree polynominal term
from sklearn.preprocessing import PolynomialFeatures

X1 = np.array([258.0, 270.0, 294.0,
               320.0, 342.0, 368.0,
               396.0, 446.0, 480.0,
               586.0])[:, np.newaxis]
y1 = np.array([236.4, 234.4, 252.8,
               298.6, 314.2, 342.2,
               360.8, 368.0, 391.2,
               390.8])[:, np.newaxis]
lr = LinearRegression()
pr = LinearRegression()
quadratic = PolynomialFeatures(degree=2)
X_quad = quadratic.fit_transform(X1)

##2. fit a sample linear regression model for comparison
lr.fit(X1, y1)
X_fit = np.arange(250, 600, 10)[:, np.newaxis]
y_lin_fit = lr.predict(X_fit)

##3. fit a multiple regression model on the transformed features for polynominal regression
pr.fit(X_quad, y1)
y_quad_fit = pr.predict(quadratic.fit_transform(X_fit))

plt.scatter(X1, y1, label='training points')
plt.plot(X_fit, y_lin_fit, label='linear fit', linestyle='--')
plt.plot(X_fit, y_quad_fit, label='quadratic fit')
plt.legend(loc='upper left')
plt.show()

y_lin_pred = lr.predict(X1)
y_quad_pred = pr.predict(X_quad)
print('Training MSE linear: {0:.3f}, quadratic: {1:.3f}'.format(
        mean_squared_error(y1, y_lin_pred),
        mean_squared_error(y1, y_quad_pred)))
print('Training R^2 linear: {0:.3f}, quadratic: {1:.3f}'.format(
        r2_score(y1, y_lin_pred),
        r2_score(y1, y_quad_pred)))

#modeling nonlinear in Housing Dataset
X = df[['LSTAT']].values
y = df['MEDV'].values
regr = LinearRegression()

##create polynominal features
quadratic = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
X_quad = quadratic.fit_transform(X)
X_cubic = cubic.fit_transform(X)

##linear fit
X_fit = np.arange(X.min(), X.max(), 1)[:, np.newaxis]
regr = regr.fit(X, y)
y_lin_fit = regr.predict(X_fit)
linear_r2 = r2_score(y, regr.predict(X))

##quadratic fit
regr = regr.fit(X_quad, y)
y_quad_fit = regr.predict(quadratic.fit_transform(X_fit))
quadratic_r2 = r2_score(y, regr.predict(X_quad))

##cubic fit
regr = regr.fit(X_cubic, y)
y_cubic_fit = regr.predict(cubic.fit_transform(X_fit))
cubic_r2 = r2_score(y, regr.predict(X_cubic))

plt.scatter(X, y, label='training points', color='lightgray')
plt.plot(X_fit, y_lin_fit, label='liner (d=1), $R^2={:.2f}$'.format(linear_r2),
         color='blue', lw=2, linestyle=':')
plt.plot(X_fit, y_quad_fit, label='quadratic (d=2), $R^2={:.2f}$'.format(quadratic_r2),
         color='red', lw=2, linestyle='-')
plt.plot(X_fit, y_cubic_fit, label='liner (d=3), $R^2={:.2f}$'.format(cubic_r2),
         color='green', lw=2, linestyle='--')
plt.xlabel('% lower status of the population [LASTA]')
plt.ylabel('Price in $1000\'s [MEDV]')
plt.legend(loc='upper rigth')
plt.show()

#transform features
X_log = np.log(X)
y_sqrt = np.sqrt(y)

##fit features
X_fit = np.arange(X_log.min()-1, X_log.max()+1, 1)[:, np.newaxis]
regr = regr.fit(X_log, y_sqrt)
y_lin_fit = regr.predict(X_fit)
linear_r2 = r2_score(y_sqrt, regr.predict(X_log))

##plot results
plt.scatter(X_log, y_sqrt, label='training points', color='lightgray')
plt.plot(X_fit, y_lin_fit, label='linear (d=1), $R^2={:.2f}$'.format(linear_r2),
         color='blue', lw=2)
plt.xlabel('log(% lower status of the population [LASTA])')
plt.ylabel('$\sqrt{Price in $1000\'s [MEDV]}$')
plt.legend(loc='lower left')
plt.show()
