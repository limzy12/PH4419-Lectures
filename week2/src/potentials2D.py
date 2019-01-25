## Calculate and plot the electric potential due to N charges distributed randomly on a plane

from scipy import *
from numpy import meshgrid as mgrid
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm as norm
import numpy as np

def potential(X, Y, xc, yc, qc, radius = 5e-2):
    assert xc.ndim == yc.ndim == qc.ndim == 1
    assert X.ndim == Y.ndim == 2
    assert len(xc) == len(yc) == len(qc)
    assert radius > 0

    phi = zeros(shape(X))

    for j in range(len(xc)):
        dist = np.power((np.power(X - xc[j], 2) + np.power(Y - yc[j], 2)), 0.5)
        dphi = qc[j] / dist
        dphi[dist < radius] = qc[j] / radius
        phi += dphi
    return phi

N = 3
Xsample = linspace(-10, 10, 200)
Ysample = linspace(-10, 10, 200)
X,Y = mgrid(Xsample, Ysample)

from scipy.stats import uniform
xc = uniform(loc = -4.5, scale = 9).rvs(size = N)
yc = uniform(loc = -4.5, scale = 9).rvs(size = N)
qc = ones(N)

phi = potential(X, Y, xc, yc, qc)


fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X,Y,phi, cmap = cm.coolwarm, linewidth = 1)
fig.show()