### Write a function to solve the Van der Pol equation using the DOPRI5 ODE solver
from scipy import *
import matplotlib.pyplot as plt


from scipy.integrate import ode


## Define the system of DEs; the first argument is the integrating variable.
def diffeq(t, y, mu): 
    x = y[0]
    v = y[1]
    return [v, mu * (1 - (x ** 2)) * v - x]

def vanderpol_plot(x0, v0, t1 = 50., nt = 2000, mu = 10., solver = 'dopri5'):
    t = linspace(0, t1, nt)
    y0 = array([x0, v0])
    y = zeros((nt, 2))

    y[0] = y0

    problem = ode(diffeq)
    problem.set_initial_value(y0)
    problem.set_integrator(solver)
    problem.set_f_params(mu)

    for i in range(1, len(t)):
        problem.integrate(t[i])
        y[i] = problem.y 

    plt.figure(1)
    plt.plot(t, y[:, 0]) # plot only the position
    xmin, xmax = 0, t1
    ymax, ymin = min(y[:, 0]) - 0.2, max(y[:, 0]) + 0.2
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    plt.show()
    

# vanderpol_plot(0.1, 0.)

## Here we play around with the parameters

# vanderpol_plot(0.1, 0., 3000., 2000, 1000.)
# vanderpol_plot(0.1, 0., 3000., 20000, 1000.)
# vanderpol_plot(0.1, 0., 3000., 20000, 1000., 'lsoda')
vanderpol_plot(0.1, 0., 3000., 2000, 1000., 'lsoda')
