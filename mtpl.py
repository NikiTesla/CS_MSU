import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100, 100, 1)
y = x ** 3

print(y)
plt.plot(x, y,  '-r')
plt.show()

