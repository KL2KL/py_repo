import matplotlib.pyplot as plt
from sympy import Symbol

def linear(total):

    X = []
    Y = []
    Z = []
    n = []

    for i in range(1,101):
        X.append(i)
        Y.append(2*i - 30)
        Z.append(4*i - 75)
        n.append(i + Y[i-1] + Z[i-1])

    m = n.index(total)
    print('X =',X[m],',','Y =',Y[m],',','Z =',Z[m])
    plt.plot(X,X)
    plt.plot(X,Y, 'c')
    plt.plot(X,Z, 'g')
    plt.plot(X,n, 'r')
    plt.axvline(x=m+1, color = 'k')
    plt.grid()
    plt.show()

print('Enter the value for Total :')
total = input()
int_total = int(total)
x = Symbol('x')
y = 2*x - 30
z = 4*x - 75
function = x + y + z
yprime = function.diff(x)

while int_total % yprime != 0:
    int_total = int_total + 1

print('Total is :', int_total)  
linear(int_total)



