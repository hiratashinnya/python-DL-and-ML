# import module
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn import model_selection
from sklearn import metrics
import matplotlib.pyplot as plt

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
# print("/*"+"="*10+"*/")
print("X_info = ", X.info)
print("Y_info = ", Y.info)

# set model
clf = linear_model.LinearRegression()
T_score = []
mse = []
for i in range(1, 10):
    print("test size = ", 0.1*i)
    # split data to training & test
    X_train, X_test, Y_train, Y_test=model_selection.train_test_split(X, Y, test_size=0.1*i)
    """ print("size of training data:(explanatory variable)(response variable)")
    print(X_train.shape, Y_train.shape)
    print("size of test data:(explanatory variable)(response variable)")
    print(X_test.shape, Y_test.shape) """
    # learning
    clf.fit(X_train, Y_train)
    # print("Regression coefficient = ", clf.coef_)
    # print("Intercept = ", clf.intercept_)
    # print("Score = ", clf.score(X_train, Y_train))
    # predict
    print("/*"+"="*10+f" result of test_size({0.1*i}) "+"="*10+"*/")
    print("Test Score = ", clf.score(X_test, Y_test))
    T_score.append(clf.score(X_test, Y_test))
    Yp = clf.predict(X_test)
    mse.append(metrics.mean_squared_error(Y_test, Yp))
    print("MSE of TestSet = ", mse[i-1])

# print average
print("/*"+"="*10+" Average of results "+"="*10+"*/")
print("average of SCORE = ", sum(T_score) / len(T_score))
print("average of MSE = ", sum(mse) / len(mse))

# plot
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.suptitle("Score & MSE of Boston & Test_Size")
ax2.set_xlabel("Test Size")
ax1.set_ylabel("Score")
ax2.set_ylabel("MSE")
xx = np.arange(0.1, 1.0, 0.1)
ax1.scatter(xx, T_score)
ax2.scatter(xx, mse)
fig.legend()
ax1.grid()
ax2.grid()
fig.show()

fig.savefig('./Score & MSE of Boston & Test_Size.png')