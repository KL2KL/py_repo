#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:22:45 2019

@author: KL2KL
"""

def find_group(n,m):
    candidate = []
    v = det_block(n,m)
    candidate1 = block_candidate(v) + extend(n,m)
    candidate2 =  final(candidate1)
    
    for i in range(21):
        k = candidate2[i]
        candidate.append(str(k[0])+str(k[1]))
        
    return candidate
    
def det_block(n,m):
    
    if n < 4 and m < 4:
        block = 1
        
    elif n < 4 and m > 3 and m < 7:
        block = 2
        
    elif n < 4 and m > 6:
        block = 3
        
    elif n > 3 and n < 7 and m < 4:
        block = 4
        
    elif n > 3 and n < 7 and m > 3 and m < 7:
        block = 5
        
    elif n > 3 and n < 7 and m > 6:
        block = 6
        
    elif n > 6 and m < 4:
        block = 7
        
    elif n > 6 and m > 3 and m < 7:
        block = 8
        
    else:
        block = 9
        
    return block
    
def block_candidate(block): # Not modify yet
    m = []
    
    if block == 1:
        
        for i in range(1,4):      
            for j in range(1,4):          
                u = [i,j]
                m.append(u)
                
    elif block == 2:
        
        for i in range(1,4):     
            for j in range(4,7):
                u = [i,j]
                m.append(u)
                
    elif block == 3:
        
        for i in range(1,4):   
            for j in range(7,10):
                u = [i,j]
                m.append(u)
                
    elif block == 4:
        
        for i in range(4,7):
            for j in range(1,4):
                u = [i,j]
                m.append(u)
    elif block == 5:
        
        for i in range(4,7):     
            for j in range(4,7):
                u = [i,j]
                m.append(u)
                
    elif block == 6:
        
        for i in range(4,7):   
            for j in range(7,10):
                u = [i,j]
                m.append(u)
                
    elif block == 7:
        
        for i in range(7,10):
            for j in range(1,4):
                u = [i,j]
                m.append(u)
                
    elif block == 8:
        
        for i in range(7,10):     
            for j in range(4,7):
                u = [i,j]
                m.append(u)
                
    else:
        
        for i in range(7,10):
            for j in range(7,10):
                u = [i,j]
                m.append(u)    
    
    return m
    
def extend(n,m):
    extend = []
    l = 9
    
    for i in range(1,l+1):
        u = [n,i]
        extend.append(u)
        
    for j in range(1,l+1):
        v = [j,m]
        extend.append(v)
     
    return extend

def final(duplicate): 
    final_list = []
    
    for n in duplicate:
        
        if n not in final_list: 
            final_list.append(n) 
            
    return final_list 

'''
def find_group(n):
    if n == '111':
        group = ['111', '112', '121', '122',
                 '211', '212',
                 '311', '321']
    elif n == '112':
        group = ['111', '112', '121', '122',
                 '211', '212',
                 '312', '322']
    elif n == '121':
        group = ['111', '112', '121', '122',
                 '221', '222',
                 '311', '321']
    elif n == '122':
        group = ['111', '112', '121', '122',
                 '221', '222',
                 '312', '322']
        ##########################################
    elif n == '211':
        group = ['211', '212', '221', '222',
                 '111', '112',
                 '411', '421']
    elif n == '212':
        group = ['211', '212', '221', '222',
                 '111', '112',
                 '412', '422']
    elif n == '221':
        group = ['211', '212', '221', '222',
                 '121', '122',
                 '411', '421']
    elif n == '222':
        group = ['211', '212', '221', '222',
                 '121', '122',
                 '412', '422']
        ############################################
    elif n == '311':
        group = ['311', '312', '321', '322',
                 '111', '121',
                 '411', '412']
    elif n == '312':
        group = ['311', '312', '321', '322',
                 '112', '122',
                 '411', '412']
    elif n == '321':
        group = ['311', '312', '321', '322',
                 '111', '121',
                 '421', '422']
    elif n == '322':
        group = ['311', '312', '321', '322',
                 '112', '122',
                 '421', '422']
        ###########################################
    elif n == '411':
        group = ['411', '412', '421', '422',
                 '211', '221',
                 '311', '312']
    elif n == '412':
        group = ['411', '412', '421', '422',
                 '212', '222',
                 '311', '312']
    elif n == '421':
        group = ['411', '412', '421', '422',
                 '211', '221',
                 '321', '322']
    elif n == '422':
        group = ['411', '412', '421', '422',
                 '212', '222',
                 '321', '322']
    else:
        group = 0
        
    return group
'''