#import module
import scipy.cluster.hierarchy as hclst
from matplotlib import pyplot as plt
import numpy as np

# data
data = [[1,2], [3,1], [2,3], [3,6], [4,6], [7,2], [7,4]]
pdata = np.array(data)

# print data
for no, d in enumerate(data):
    print("No = ", no, ", data = ", d)

# ready for plot
fig, axes = plt.subplots(1, 3, sharex=True, sharey=False)
fig.suptitle("Dendrogram of Hierarchy Clustering")
axes[0].set_ylabel("distance")

methods = ["single","complete", "ward"]
for i, meth in enumerate(methods):
    # clustering
    results = hclst.linkage(data, method=meth, metric='euclidean')
    hclst.dendrogram(results, ax=axes[i]) # plot dendrogram
    axes[i].set_xlabel("data number")
    axes[i].set_title(meth)

# output figure
fig.show()
fig.savefig("Dendrogram of Hierarchy Clustering.png")