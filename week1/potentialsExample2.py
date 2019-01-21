## Plotting the electric potential of charges along a line

from scipy import *
import matplotlib.pyplot as plt

def potential(X, xc, qc):
    M = len(X)      # Number of sampling points
    N = len(xc)     # Number of charges
    phi = zeros(M)
    for j in range(N):
        phi += qc[j] / abs(X - xc[j]) # Calculate and add potentials for each charge
    return phi

charges_x = array([-0.2, 0.2])
charges_q = array([-0.1, 1.5])
xplot = linspace(-3,3,500)

phi = potential(xplot, charges_x, charges_q)

plt.plot(xplot, phi)
plt.show()
