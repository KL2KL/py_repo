#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Aug 15 13:22:53 2019
    
    @author: KL2KL
    """

import g2

def printBoard(board):
    print(board['11'] + '|' + board['12'] + '|' + board['13'] + '|' + board['14'] + '|' + board['15'] + '|' + board['16'] + '|' + board['17'] + '|' + board['18'] + '|' + board['19'])
    print('-+-+-+-+-+-+-+-+-')
    print(board['21'] + '|' + board['22'] + '|' + board['23'] + '|' + board['24'] + '|' + board['25'] + '|' + board['26'] + '|' + board['27'] + '|' + board['28'] + '|' + board['29'])
    print('-+-+-+-+-+-+-+-+-')
    print(board['31'] + '|' + board['32'] + '|' + board['33'] + '|' + board['34'] + '|' + board['35'] + '|' + board['36'] + '|' + board['37'] + '|' + board['38'] + '|' + board['39'])
    print('-+-+-+-+-+-+-+-+-')
    print(board['41'] + '|' + board['42'] + '|' + board['43'] + '|' + board['44'] + '|' + board['45'] + '|' + board['46'] + '|' + board['47'] + '|' + board['48'] + '|' + board['49'])
    print('-+-+-+-+-+-+-+-+-')
    print(board['51'] + '|' + board['52'] + '|' + board['53'] + '|' + board['54'] + '|' + board['55'] + '|' + board['56'] + '|' + board['57'] + '|' + board['58'] + '|' + board['59'])
    print('-+-+-+-+-+-+-+-+-')
    print(board['61'] + '|' + board['62'] + '|' + board['63'] + '|' + board['64'] + '|' + board['65'] + '|' + board['66'] + '|' + board['67'] + '|' + board['68'] + '|' + board['69'])
    print('-+-+-+-+-+-+-+-+-')
    print(board['71'] + '|' + board['72'] + '|' + board['73'] + '|' + board['74'] + '|' + board['75'] + '|' + board['76'] + '|' + board['77'] + '|' + board['78'] + '|' + board['79'])
    print('-+-+-+-+-+-+-+-+-')
    print(board['81'] + '|' + board['82'] + '|' + board['83'] + '|' + board['84'] + '|' + board['85'] + '|' + board['86'] + '|' + board['87'] + '|' + board['88'] + '|' + board['89'])
    print('-+-+-+-+-+-+-+-+-')
    print(board['91'] + '|' + board['92'] + '|' + board['93'] + '|' + board['94'] + '|' + board['95'] + '|' + board['96'] + '|' + board['97'] + '|' + board['98'] + '|' + board['99'])


def get_candidate(n):
    offer = theBoard[n]
    
    if offer != ' ':
        x = int(offer)
        
        if x not in flag:
            default.remove(x)
            flag.append(x)
            #result_list[int(n)] = [0]

    return default

def generate_list(v,default,flag):
    
    if v not in confirmed:
        n = int(int(v)/10)
        m = int(v)%10
        group1 = g2.find_group(n,m)
        
        for i in range(21):
            m = group1[i]
            candidate1 = get_candidate(m)
            if default == []:
                candidate1 = [0]

    else:
        candidate1 = [0]
    
    return candidate1

def mod_index(n):
    if n == 0:
        w = 10
        
    else:
        a = [1,2,3,4,5,6,7,8,9]
        b = n % 9
        
        if b == 0:
            k = a[8]
        
        k = a[b - 1]
        
        if n % 9 == 0:
            v = int(n / 9)
        
        else:
            v = int(n / 9) + 1
        
        w = str(v) + str(k)
    
    return w

def check_known(result_list):
    found1 = 0
    found2 = 0
    for p in range(1,82):
        if len(result_list[p-1]) == 1 and result_list[p-1] != [0]:
            p_value = result_list[p-1]
            p = mod_index(p)
            theBoard[p] = str(p_value[0])
            found1 = 1
            
    return ((found1 + found2),result_list)

def check_known_2(result_list):
    
    for p in range(1,82):
        if len(result_list[p-1]) == 1 and result_list[p-1] != [0]:
            p_value = result_list[p-1]
            p = mod_index(p)
            theBoard[p] = str(p_value[0])
            
    return (result_list)

def two_row():
    index = []
    u = 0
    for i in range(81):
        index.append(len(result_list[i]))
        if len(result_list[i]) == 2:
            u = u + 1
            if u > 6:
                u = 6
    for i in range(1,3):
        for j in range(1,3):
            for k in range(1,3):
                for l in range(1,3):
                    for m in range(1,3):
                        for o in range(1,3):                
                            a = (i,j,k,l,m,o)
                            a = a[6-u:6]
                            row.append(a)       
              
    return (u,row[0:2**u])

def three_row():
    u = 0
    for i in range(81):
        result_list.append(len(result_list[i]))
        if len(result_list[i]) == 3:
            u = u + 1
            if u > 6:
                u = 6
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                for l in range(1,4):
                    for m in range(1,4):
                        for o in range(1,4):                
                            a = (i,j,k,l,m,o)
                            a = a[6-u:6]
                            row.append(a)                
                        
    return row[0:3**u]

def try_out(u,v):
    insert1.append(u)
    insert2.append(v)
    
    return (u,v)
    
    
    
    
    
        
       ############################################################################################3
    
theBoard = {'11' : ' ', '12' : ' ', '13' : ' ', '14' : ' ', '15' : ' ', '16' : ' ', '17' : ' ', '18' : ' ', '19' : ' ',
            '21' : ' ', '22' : ' ', '23' : ' ', '24' : ' ', '25' : ' ', '26' : ' ', '27' : ' ', '28' : ' ', '29' : ' ',
            '31' : ' ', '32' : ' ', '33' : ' ', '34' : ' ', '35' : ' ', '36' : ' ', '37' : ' ', '38' : ' ', '39' : ' ',
            '41' : ' ', '42' : ' ', '43' : ' ', '44' : ' ', '45' : ' ', '46' : ' ', '47' : ' ', '48' : ' ', '49' : ' ',
            '51' : ' ', '52' : ' ', '53' : ' ', '54' : ' ', '55' : ' ', '56' : ' ', '57' : ' ', '58' : ' ', '59' : ' ',
            '61' : ' ', '62' : ' ', '63' : ' ', '64' : ' ', '65' : ' ', '66' : ' ', '67' : ' ', '68' : ' ', '69' : ' ',
            '71' : ' ', '72' : ' ', '73' : ' ', '74' : ' ', '75' : ' ', '76' : ' ', '77' : ' ', '78' : ' ', '79' : ' ',
            '81' : ' ', '82' : ' ', '83' : ' ', '84' : ' ', '85' : ' ', '86' : ' ', '87' : ' ', '88' : ' ', '89' : ' ',
            '91' : ' ', '92' : ' ', '93' : ' ', '94' : ' ', '95' : ' ', '96' : ' ', '97' : ' ', '98' : ' ', '99' : ' '}

theBoard['12'] = '3'
theBoard['15'] = '7'
theBoard['21'] = '6'
theBoard['24'] = '1'
theBoard['26'] = '5'
theBoard['32'] = '9'
theBoard['33'] = '8'
theBoard['38'] = '6'
theBoard['41'] = '8'
theBoard['45'] = '6'
theBoard['49'] = '3'
theBoard['51'] = '4'
theBoard['56'] = '3'
theBoard['59'] = '1'
theBoard['61'] = '7'
theBoard['65'] = '2'
theBoard['69'] = '6'
theBoard['72'] = '6'
theBoard['77'] = '2'
theBoard['78'] = '8'
theBoard['84'] = '4'
theBoard['85'] = '1'
theBoard['86'] = '9'
theBoard['89'] = '5'
theBoard['95'] = '8'
theBoard['98'] = '7'
theBoard['99'] = '9'

theBoard_t = theBoard.copy()

confirmed = ['12', '15', '21', '24',
             '26', '32', '33', '38', '41', '45',
             '49', '51', '56', '59', '61',
             '65', '69', '72', '77', '78', '84',
             '85', '86', '89', '95', '98', '99']

#confirmed does matter !

printBoard(theBoard)
print()
insert1 = []
insert2 = []
for i in range(20): #13 
    
    result_list = []
    
    for m in range(1,10):
        for k in range(1,10):
            default = [1,2,3,4,5,6,7,8,9]
            flag = []
            v = str(m) + str(k)
            w = generate_list(v,default,flag)
            result_list.append(w)
    
    (found,result_list) = check_known(result_list)
    theBoard_end = theBoard.copy()
    #print()
    if found == 0 and not all(0 in sl for sl in result_list):
        
        theBoard_t = theBoard
        row = []
        u_list = []
        (n,row) = two_row()
        result_list_t = result_list.copy()
        
        z = 0
        for i in range(64):
     
            k = 0
            
            for j in range(81):
                
                if len(result_list_t[j]) == 2 and k < 6:
                    result_list_t[j] = [result_list_t[j][row[i][k]-1]]
                    u = mod_index(j+1)
                    v = result_list_t[j]
                    u_list.append(u)
                    u_list1 = u_list[0:6]
                    
                    theBoard[u] = str(v[0])
                    insert2.append(v)
                    k = k + 1
                    
                    if k == 6:
                        
                        if all(0 in sl for sl in result_list_t):
                            
                            #printBoard(theBoard)
                            break
                        else:
                            result_list_t = result_list.copy()
                      
                            
                        for i in range(6):
                            confirmed.append(u_list1[i])
                            insert1.append(u_list1[i])
    #p = 1                       
    #while True:
        for y in range(0,36):#(35,36)
            for i in range((y+1)*6-6, (y+1)*6):#384
                u = insert1[i]
                v = insert2[i]
                #print(u,v)
                theBoard[u] = str(v[0])
        
        #p = p + 1
        
    if all(0 in sl for sl in result_list):
        
        printBoard(theBoard)
        break    
        
    
