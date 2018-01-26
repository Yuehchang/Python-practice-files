#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:44:33 2018

@author: changyueh
"""

#The original boosting procedure steps page224
exec(open('/users/changyueh/desktop/codepractice/machine_learning/chapt7/3_bagging.py').read())

from sklearn.ensemble import AdaBoostClassifier

tree = DecisionTreeClassifier(criterion='entropy', max_depth=1,
                              random_state=0)
ada = AdaBoostClassifier(base_estimator=tree, n_estimators=500,
                         learning_rate=0.1, random_state=0)
tree = tree.fit(X_train, y_train)
y_train_pred = tree.predict(X_train)
y_test_pred = tree.predict(X_test)
tree_train = accuracy_score(y_train, y_train_pred)
tree_test = accuracy_score(y_test, y_test_pred)
print('Decision tree train/test accuracies {0:.3f}/{1:.3f}'.format(tree_train, tree_test))

ada = ada.fit(X_train, y_train)
y_train_pred = ada.predict(X_train)
y_test_pred = ada.predict(X_test)
ada_train = accuracy_score(y_train, y_train_pred)
ada_test = accuracy_score(y_test, y_test_pred)
print('AdaBoost train/test accuracies {0:.3f}/{1:.3f}'.format(ada_train, ada_test))
