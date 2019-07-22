#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:39:03 2019

@author: KL2KL
"""
import sys

def income_cal(bonus, mysale, unit, level):
    point = 2500
    
    if bonus == 0:
        print('How many units has your team sold totally ?')
        unit = int(input())
    
    c1 = 0.12
    c2 = [0, 0, 0.08, 0.12, 0.13, 0.14, 0.15, 0.16]
    c31 = [0, 0, 1, 1, 1, 1, 1, 1]
    c3 = [(bonus*100*x) for x in c31]
    c4 = [0, 0, 0, 0, 1, 1, 1, 1]
    
    if level[0] > 8:
        print('argument for level is between 1 - 8.')
        sys.exit()

    pv = unit * point
    y1 = pv * (c1 + c2[level[0]-1] + c3[level[0]-1]/pv + c4[0])
    share = 0
    
    for i in range(level[0]-3):
        share = share + level[i+1] * c2[i+2]

    deduction = point * share + mysale * point * c1
    y = y1 - deduction
    yjb = []
    yjm = []
    yjg = []
    yjr = []
    for i in range(unit-10, unit+21, 10):
        pvi = i * point
        
        for j in range(8):
            yj = pvi * (c1 + c2[j] + c3[level[0]-1]/pv + c4[0]) - deduction
            
            if i == unit - 10:
                yjb.append(yj)
            elif i == unit:
                yjm.append(yj)
            elif i == unit + 10:
                yjg.append(yj)
            else:
                yjr.append(yj)
    
    return round(y), yjb, yjm, yjg, yjr
    
         
    



        