import matplotlib.pyplot as plt
#Importing the fft and inverse fft functions from fftpackage
import numpy as np
from scipy.fftpack import fft

#create an array with random n numbers
#x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
resolution = 501
w = 100
x = np.linspace(0, w*2*np.pi, resolution)
x = np.sin(x)
#Applying the fft function
y = fft(x)
plt.plot(abs(y)/resolution)
plt.grid()
plt.show()

