from scipy import *
import numpy as np
import matplotlib.pyplot as plt

def fnInt(x): ## This defines the function to be integrated.
    return x


xMin = 0
xMax = 1
dx = 0.001
numPts = (xMax - xMin)/dx
X = linspace(xMin, xMax, numPts)
Y = zeros(len(X))
result = 0

for i in range(len(X)):
    Y[i] = fnInt(X[i])

for i in (range(len(X) - 1)):
    result += (Y[i+1] + Y[i]) * (dx / 2)

print(result)