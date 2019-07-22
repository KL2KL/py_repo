#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:46:09 2019

@author: KL2KL
"""
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from scipy.fftpack import fft

p = pyaudio.PyAudio()
print('Please enter the frequency :')
f = int(input())
print('Please enter the sampling rate :')
fs = int(input()) + 1
duration = 5
#wt = np.linspace(0, 2*np.pi*f, fs)
#wt = w*(0:rate*duration-1)/rate;
#x = np.sin(wt).astype(np.float32)
    
x = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32).tobytes()
x1 = (np.sin(2*np.pi*np.arange(fs)*f/fs)).astype(np.float32)
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

stream.write(x)
stream.stop_stream()
stream.close()
p.terminate()

y = fft(x1)
plt.plot(x1)
plt.grid()
plt.xlim(0, f/10)
plt.show()
plt.plot(abs(y)/fs)
plt.grid()
plt.show()
