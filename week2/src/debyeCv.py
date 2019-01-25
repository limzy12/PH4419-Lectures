##  Numerical integration of Heat Capacity in Debye's model

from scipy import *
import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate


def integrand(x):
    return ((x ** 4) * exp(x)) / (exp(x) - 1) ** 2

def cv(T):
    vol = 1e-3
    rho = 6.022e28
    debyeT = 428.
    K_B = 1.38e-23

    uppLimit = debyeT / T

    integral = integrate.quad(integrand, 0., uppLimit)
    coeff = 9 * vol * rho * K_B / (uppLimit ** 3)

    return coeff * integral[0]

def plotCv(lowerT, upperT, numPts):
    T = linspace(lowerT, upperT, numPts)
    Cv = np.zeros(len(T))
    
    for i in range(len(T)):
        Cv[i] = cv(T[i])
    
    plt.plot(T, Cv)
    plt.show()

plotCv(5,500, 100)