#import module
import scipy.cluster.hierarchy as hclst
from matplotlib import pyplot as plt
import numpy as np

# data (add 1 point)
data = [[1,2], [3,1], [2,3], [3,6], [4,6], [7,2], [7,4], [5,4]]
pdata = np.array(data)

# print data
for no, d in enumerate(data):
    print("No = ", no, ", data = ", d)

# methods & metrics to use
methods = ["single","complete"]#, "ward"]
metrics = ["euclidean", "minkowski", "canberra"]

# ready for plot
fig, axes = plt.subplots(len(metrics), len(methods), sharex=True, sharey=False, tight_layout=True)
fig.suptitle("Exercise3 : Dendrogram of Hierarchy Clustering")

for i in range(len(methods)):
    axes[-1][i].set_xlabel("data number")

for j in range(len(metrics)):
    axes[j][0].set_ylabel("distance")

for j, metr in enumerate(metrics):
    for i, meth in enumerate(methods):
        # clustering
        results = hclst.linkage(data, method=meth, metric=metr)
        hclst.dendrogram(results, ax=axes[j][i]) # plot dendrogram
        axes[j][i].set_title(metr+":"+meth)

# output figure
fig.show()
fig.savefig("Exercise3_Dendrogram of Hierarchy Clustering.png")