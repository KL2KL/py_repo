#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:07:36 2020

@author: KL2KL
"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def compound(principle,deposit,rate,freq,years):
    t = np.linspace(1, 1, years*freq)
    t = deposit * t     
    t = np.insert(t,0,principle)
    answer_array = signal.lfilter([1], [1,-(rate/freq + 1)], t)
    plt.plot(answer_array, 'r')
    plt.grid()
    deposit_array = signal.lfilter([1], [1,-1], t)
    plt.plot(deposit_array, 'b')
    plt.show()
    result = answer_array[years*freq]
    
    return result

print('enter your principle :')
principle = int(input())
print()
print('enter the amount you deposit after :')
deposit = int(input())
print()
print('enter your interest rate :')
rate = float(input())
print()
print('compound monthly(12) or annually(1) :')
freq = int(input())
print()
print('how many years to calculate ?')
years = int(input())
print()
u = compound(principle,deposit,rate,freq,years)
print()
print(u)

