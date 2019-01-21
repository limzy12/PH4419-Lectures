## Plotting the electric potential of a charge along a line

from scipy import *
import matplotlib.pyplot as plt

x0 = 1.5 
q0 = 1.0

X = linspace(0, 1.6, 500)
phi = q0 / abs(X - x0)

plt.plot(X, phi)
plt.show()