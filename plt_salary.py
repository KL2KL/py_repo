#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:54:04 2019

@author: KL2KL
"""
import matplotlib.pyplot as plt
import numpy as np
import sys, ast
import salary

if len(sys.argv) != 3:
    print('Usage: python3 salary.py bonus mysale (you must enter 2 arguments.)')
    sys.exit()

bonus = int(sys.argv[1])
mysale = int(sys.argv[2])
print('Enter your level and share structure: ')
level = input()
level = ast.literal_eval(level)
unit = bonus + mysale
y, yjb, yjm, yjg, yjr = salary.income_cal(bonus, mysale, unit, level)   
print(y) 
x = np.arange(1,9)            
plt.plot(x,yjb,'bo')
plt.plot(x,yjm,'mo')
plt.plot(x,yjg,'go')
plt.plot(x,yjr,'ro')
plt.grid()
plt.show()


