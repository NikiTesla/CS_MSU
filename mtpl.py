from matplotlib import pyplot as mp
import numpy as np

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

mu = 4
sig = 1

x_values = np.linspace(-3, 3, 120)
mp.plot(x_values, gaussian(x_values, mu, sig))

mp.show()