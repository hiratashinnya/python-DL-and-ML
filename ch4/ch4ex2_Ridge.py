# import module
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn import model_selection
from sklearn import metrics

# ready data
boston = load_boston()
""" print("/*"+"="*10+"*/")
print(boston['DESCR'])
print("/*"+"="*10+"*/")
print(boston['data'])
print("/*"+"="*10+"*/")
print(boston['feature_names']) """
X = pd.DataFrame(boston['data'], columns=boston['feature_names'])
Y = pd.DataFrame(boston['target'])
print("/*"+"="*10+"*/")
print("X_info = ", X.info)
print("Y_info = ", Y.info)

# set model
clf = linear_model.Ridge(alpha=0.5)

# split data to training & test
X_train, X_test, Y_train, Y_test=model_selection.train_test_split(X, Y, test_size=0.3)
print("size of training data:(explanatory variable)(response variable)")
print(X_train.shape, Y_train.shape)
print("size of test data:(explanatory variable)(response variable)")
print(X_test.shape, Y_test.shape)

# learning
clf.fit(X_train, Y_train)
print("Regression coefficient = ", clf.coef_)
print("Intercept = ", clf.intercept_)
print("Score = ", clf.score(X_train, Y_train))

# predict
print("Test Score = ", clf.score(X_test, Y_test))
Yp = clf.predict(X_test)
mse = metrics.mean_squared_error(Y_test, Yp)
print("MSE of TestSet = ", mse)