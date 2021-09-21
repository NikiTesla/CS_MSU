import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


x = np.arange(-100, 100, 1)
print(x)

y = x ** 3
print(y)
plt.plot(x, y, '-r')
plt.show()

print("Hello")
