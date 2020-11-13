#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:34:30 2020

@author: KL2KL
"""
import sys
import time

if len(sys.argv) != 2:
    print('Usage: python3 bottle.py [bottles] (you must enter only one argument.)')
    sys.exit()

number_text = sys.argv[1]
start = time.time()

number = int(number_text)
counter = number
B_group = number
C_group = number
b = 1
c = 0

while b or c:
    b = int(B_group / 2)
    c = int(C_group / 4)
    bremainder = B_group % 2
    cremainder = C_group % 4
    addon_bottle = b + c
    counter = counter + addon_bottle
    B_group = bremainder + addon_bottle
    C_group = cremainder + addon_bottle

y = counter
print(y)

end = time.time()
print(end-start)
