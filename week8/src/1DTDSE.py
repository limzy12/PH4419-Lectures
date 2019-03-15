from scipy import *
import matplotlib.pyplot as plt

import numpy as np
import numpy.linalg as la

def constructMatrix(mu, N):
    diag0 = zeros((N), dtype = np.complex64) + (1. + mu)
    diag1 = zeros((N-1), dtype = np.complex64) + (-0.5 * mu)
    returnMat = diag(diag0, 0) + diag(diag1, 1) + diag(diag1, -1)
    return returnMat

L = 1.e-8
x0 = L / 2.
sigma = 1.e-10
kappa = 5.e10
N = 1000
m = 9.11e-31
hbar = 1.05e-34


x = linspace(0., L, N)
dx = L / N
dt = 1.e-18

psi = exp(- (x - x0)**2 / (2 * sigma ** 2)) * exp(1j * kappa * x)

mu = (1j * dt * hbar) / (2 * dx**2 * m)

A = constructMatrix(mu, N)
B = constructMatrix(-1 * mu, N)

for time in range(3000):
    psi_new = matmul(la.inv(A), matmul(B, psi.transpose()))
