##  Numerical integration of Heat Capacity in Debye's model

from scipy import *
import numpy as np

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
    coeff = 9 * vol * rho / (uppLimit ** 3)

    return coeff * integral[0]

print(cv(300))