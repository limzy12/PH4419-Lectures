from scipy import *
import matplotlib.pyplot as plt

import scipy.fftpack as fft

DJI = loadtxt('dow.txt', float)
N = len(DJI)

ftDJI = fft.rfft(DJI)
ftN = len(ftDJI)

ftDJI[int(0.05 * ftN):] = 0.
newDJI = fft.irfft(ftDJI)

plt.figure(1)
plt.plot(range(N), DJI)
plt.plot(range(N), newDJI)
plt.show()