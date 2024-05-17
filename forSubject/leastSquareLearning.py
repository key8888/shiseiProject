import numpy as np
from matplotlib import pyplot as plt

x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])

a = np.dot(x, y) / (x ** 2).sum()
print(np.dot(x, y))
plt.scatter(x, y, color='k')
plt.plot(0, x.max(), [0, a * x.max()])
plt.xlim(-0.5, 7.5)
plt.ylim(-0.5, 5.5)
plt.show()
