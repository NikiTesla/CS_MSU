import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = 1 / x

print(y)
plt.plot(x, y,  '-r')
plt.show()

