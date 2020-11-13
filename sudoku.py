#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Aug 15 13:22:53 2019
    
    @author: KL2KL
    """

import groups

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

    return default

def generate_list(v):
    
    if v not in confirmed:
        n = int(int(v)/10)
        m = int(v)%10
        group1 = groups.find_group(n,m)
        
        for i in range(21):
            m = group1[i]
            candidate1 = get_candidate(m)
            if default == []:
                candidate1 = [0]
                
    else:
        candidate1 = [0]
    
    return candidate1
'''
def my_sort(): # function unused
    my_sort = []
    
    for i in range(1,17):
        for j in range(1,5):
            v = [i,j]
            my_sort.append(v)

    return my_sort

def iterate(confirmed, q, counter):
    if counter - 1 != 0:
        c1 = result_list[q][1]
        counter = counter - 1
        print('only once')
    
    c1 = result_list[q][0]
    print(c1)
    l = q + 1
    n = ((l - 1) // 9) + 1
    v = str(int(n)) + str(int(g))
    print(v)
    theBoard[v] = str(c1)
    confirmed.append(v)
    confirmed = sorted(confirmed)
    
    return confirmed
'''
def mod_index(n):
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
            #print(p)
            #print(p_value)
            theBoard[p] = str(p_value[0])
            #print(theBoard)
            #print(v)
            #confirmed.append(v)
            #confirmed = sorted(confirmed)
            #print(confirmed)
            found1 = 1
            
    return (found1 + found2)


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

theBoard['11'] = '5'
theBoard['12'] = '3'
theBoard['15'] = '7'
theBoard['21'] = '6'
theBoard['24'] = '1'
theBoard['25'] = '9'
theBoard['26'] = '5'
theBoard['32'] = '9'
theBoard['33'] = '8'
theBoard['38'] = '6'
theBoard['41'] = '8'
theBoard['45'] = '6'
theBoard['49'] = '3'
theBoard['51'] = '4'
theBoard['54'] = '8'
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

confirmed = ['11', '12', '15', '21', '24', '25',
             '26', '32', '33', '38', '41', '45',
             '49', '51', '54', '56', '59', '61',
             '65', '69', '72', '77', '78', '84',
             '85', '86', '89', '95', '98', '99']
#confirmed_t = confirmed
printBoard(theBoard)
print()

#counter = 1
while True:
    g = 1
    for i in range(1): # for i in range(81):
        while True:
            result_list = []
            
            for m in range(1,10):
                for k in range(1,10):
                    default = [1,2,3,4,5,6,7,8,9]
                    flag = []
                    v = str(m) + str(k)
                    w = generate_list(v)
                    result_list.append(w)
        
            #print(result_list)
            #print()
            #print()
        
            found = check_known(result_list)
            #print(found)
            if found == 0:
                break
    
        #if result_list[i] != [0]:

            #test1 = iterate(confirmed, i, counter)
            #print(test1)

        #if not all(result_list):
         #   counter = counter + 1
            #print('flag on')
            #print()
            #printBoard(theBoard)
            #print()
            #confirmed = confirmed_t
            #theBoard = theBoard_t.copy()
            
            #break
        
        g = g + 1
        a = [1,2,3,4,5,6,7,8,9]
        b = g % 9
        if b == 0:
            g = a[8]
        
        g = a[b - 1]
    #counter = counter + 1
    
    printBoard(theBoard)
    
    if all(0 in sl for sl in result_list):
        break
    #print(counter)
    #if counter == 2:
        #break



