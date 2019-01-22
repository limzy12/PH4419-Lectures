from scipy import *
import numpy as np
import matplotlib.pyplot as plt

def fnInt(x): ## This defines the function to be integrated.
    return x


xMin = 0.0
xMax = 1.0
numPts = 100
dx = (xMax - xMin)/numPts

X = linspace(xMin, xMax, numPts)
Y = zeros(numPts)
result = 0

for i in range(numPts):
    Y[i] = fnInt(X[i])

for i in range(numPts - 1):
    result += (Y[i+1] + Y[i]) * (dx / 2)

print(result)