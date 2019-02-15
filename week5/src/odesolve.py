from scipy import *
import matplotlib.pyplot as plt

import scipy.integrate as intgrt

def dt(y0, t):
    omega = 1.
    mass = 1.
    x = y0[0]
    v = y0[1]
    return array([v, -1. * mass * (omega ** 2.) * x])

t = linspace(0., 30., 1000)
y0 = array([0., 1.])

sol = intgrt.odeint(dt, y0, t)

plt.figure(1)
plt.plot(t, sol[:, 0])
plt.plot(t, sol[:, 1])
plt.show()


