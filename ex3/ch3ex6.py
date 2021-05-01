import matplotlib.pyplot as plt
import numpy as np
import os

x = np.arange(0, 2, 0.01)
xpi = x*np.pi
sinx = np.sin(xpi)
cosx = np.cos(xpi)

plt.title("sin function & cos function")
plt.xlabel("rad(*$\pi$)")
plt.grid(True)
plt.plot(x, sinx, label = "sin(x)")
plt.plot(x, cosx, label = "cos(x)")
plt.legend()
plt.show()