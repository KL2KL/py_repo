#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:32:10 2019

@author: KL2KL
"""

import sys, salary, ast

if len(sys.argv) != 3:
    print('Usage: python3 min_unit.py level expected_value (you must enter 2 arguments.)')
    sys.exit()
    
level = sys.argv[1]
level = ast.literal_eval(level)

if len(level) != level[0] - 2:
        print('There are '+ str(level[0] - 3) + ' arguments followed by level.')
        sys.exit()
        
value = int(sys.argv[2])
mysale = 1
i = 0

while True:
    i = i + 1
    unit = i + mysale
    y,_,_,_,_ = salary.income_cal(i, mysale, unit, level)
    
    if y >= value:
        print(i)
        break
       
print(y)

        
        
        

