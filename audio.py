#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 09:05:41 2019

@author: KL2KL
"""
import matplotlib.pyplot as plt
import pyaudio
import numpy as np
from scipy.fftpack import fft

p = pyaudio.PyAudio()

volume = 1     # range [0.0, 1.0]
fs = 16384#44100       # sampling rate, Hz, must be integer
duration = 3   # in seconds
f1 = 700.0     # sine frequency, Hz, may be float
f2 = 1000.0
# generate samples, note conversion to float32 array

t = np.linspace(0, duration, fs*duration, endpoint=False)
samples1 = np.sin(2 * np.pi * f1 * t).astype(np.float32)
samples2 = np.sin(2 * np.pi * f2 * t).astype(np.float32)
#samples1 = (np.sin(2*np.pi*np.arange(fs*duration)*f1/fs)).astype(np.float32)
#samples2 = (np.sin(2*np.pi*np.arange(fs*duration)*f2/fs)).astype(np.float32)
samples = samples1 + samples2
# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

y = fft(samples)
plt.plot(samples)
plt.grid()
plt.xlim(0, f2/6)
plt.show()
plt.plot(np.arange(len(samples))/duration, abs(y)/(fs*duration))
plt.grid()
plt.xlim(0, fs/2)
plt.show()
stream.write((volume*samples).tobytes())
stream.stop_stream()
stream.close()

p.terminate()
