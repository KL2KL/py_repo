import time
import numpy as np
from scipy import signal

def fib(n):
    '''
    x,y = 0,1
    result = []
    while x < n:
        result.append(x)
        #a,b = b, a+b
        z = x + y
        x = y
        y = z
        #temp = b
        #b = a+b
        #a = temp  
    '''
    t = np.linspace(1, 1, number-3)
    t = np.insert(t,0,0)
    v = signal.lfilter([1], [1,-1,-1], t)
    v = v + 1
    v = np.insert(v,0,1)
    result = np.insert(v,0,0)
    
    return result

#print('enter a number for the limit of fibonacci :')
print('enter a number for n_th fibonacci series you want to show :')
number = int(input())
print()
start = time.time()
u = fib(number)

#for x in u:
    #print ('{0:1.0f}'.format(x),' ', end = '')

#print(u)   
print(u.astype(int))
print()
end = time.time()
print(end-start)

