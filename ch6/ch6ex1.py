#import module
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# data
data = [[1,2], [3,1], [2,3], [3,6], [4,6], [7,2], [7,4]]
pdata = np.array(data)
N, L = np.shape(pdata)

# center of cluster
cdata = [[2.0, 2.0], [4.0, 4.0], [6.0, 6.0]]
cdata = np.array(cdata)

# number of cluster
K = 3

# center
print("Center:")
for k in range(K):
    print(cdata[k])

# distance between center point & data point
print("Distance between Center point & Data point")
header = [f"data{n+1}" for n in range(N)]
index = [f"center{k+1}" for k in range(K)]
distance = np.empty((K, N))
for k in range(K):
    for n in range(N):
        distance[k, n] = np.sqrt(np.square(cdata[k, 0] - pdata[n, 0]) + np.square(cdata[k, 1] - pdata[n, 1]))

df = pd.DataFrame(distance, columns=header, index=index)
print(df)





"""
# plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid()
ax.scatter(pdata[:, 0], pdata[:, 1])
fig.show()
 """