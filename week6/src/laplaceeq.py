'''
Laplace equation (in thermal physics) describes the steady-state heat equation without a heat source in some region of space. 

Consider a square plate with zero temperature on three sides and T(x) = x(x - 1) on the top side. Here, we solve the Laplace equation given the Dirichlet boundary conditions and plot the temperature at each point on the plate. 

Set the grid spacing in the x and y direction to be equal
'''

from scipy import *
import matplotlib.pyplot as plt

dx = dy = 0.01
xLen = yLen = 1
xPts = (Lx / dx) + 1
yPts = (Ly / dy) + 1

x = linspace(0, xLen, int(xPts))
y = linspace(0, yLen, int(yPts))

u = zeros((int(xPts), int(yPts)))

## Setting the boundary conditions 
u[:, 0] = 0
u[:, -1] = 0
u[-1, :] = 0
u[0, :] = -1 * x * (x - 1)


u_new = copy(u)

upp_bound_err = 1e-10
max_iter = 1e5
err = 1.0
iterator = 0

while (err > upp_bound_err) and (iterator < max_iter):
    '''
    ### Naive looping, O(n^2)

    for i in range(1, int(yPts) - 1):
        for j in range(1, int(xPts) - 1): 
            u_new[i,j] = 0.25 * (u[i-1, j] + u[i+1, j] + u[i, j+1] + u[i, j-1])
    '''
    ## We can use matrix operations instead

    err = abs(mean(u_new - u))
    iterator += 1
