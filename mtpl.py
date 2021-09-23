# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(- 2 * np.pi,2 * np.pi,  np.pi/10)
y = np.sin(x)

print(y)
plt.plot(x, y,  '-r')
plt.show()  
# %%
