import numpy as np

a = np.array([[0,1],[2,3],[4,5]])
print("A=\n", a)
print("dim A:", a.ndim)
b = np.array([[6,5],[4,3],[2,1]])
print("B=\n", b)
print("dim B:", b.ndim)
c = a.T.dot(b)
print("C=\n",c)
print("dim C:", c.ndim)
print("shape C:", c.shape)