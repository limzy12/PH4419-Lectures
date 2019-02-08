from scipy import *
import matplotlib.pyplot as plt

import numpy.random as rndm

def integrand(x, y, z):
    return cos(x * y * exp(z))

def calculate_I(N):
    integral = 0
    total = 0
    for i in range(N):
        x = rndm.rand()
        y = rndm.rand()
        z = 2 * rndm.rand()

        if (y > x) and (z > (x * y)):
            integral += integrand(x, y, z)

    return integral / N * 2

def errorPlot():
    numPts = 100
    N = linspace(1,6, numPts)
    print(N)
    error = zeros(shape(N))
    for i in range(len(N)):
        error[i] = abs(0.522214 - calculate_I(int(10 ** N[i])))

    plt.figure(1)
    plt.plot(N, error, '.')
    plt.show()

print(calculate_I(100000))
errorPlot()
