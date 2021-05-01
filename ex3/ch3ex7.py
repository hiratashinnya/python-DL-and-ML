import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model as lm
import random

# response variable
l=[22200.0]
for i in range(1, 50):
    l.append(l[-1] + random.uniform(-100.0, 100.0))
nikkei = np.array(l)
L = len(nikkei)
yy = nikkei.reshape(L, 1)
print(yy)

# explanatory variable
xx = np.arange(1, L+1)
xx = xx.reshape(L, 1)
print(xx)

# create Forecast Model
clf = lm.LinearRegression()
clf.fit(xx, yy)

print("Regression coefficient = ", clf.coef_)
print("Intercept = ", clf.intercept_)
print("Score = ", clf.score(xx, yy))

# plot
plt.title("Averrage price of Nikkei stock market")
plt.xlabel("Date number")
plt.ylabel("Price(Yen)")
plt.grid()
plt.scatter(xx, yy)
plt.plot(xx, clf.predict(xx))
plt.show()
