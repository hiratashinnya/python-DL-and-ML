#import module
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# data
data = [[1,2], [3,1], [2,3], [3,6], [4,6], [7,2], [7,4]]
pdata = np.array(data)

# plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid()
ax.scatter(pdata[:, 0], pdata[:, 1])
fig.show()
