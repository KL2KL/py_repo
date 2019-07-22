import time
def fib(n):
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
    return result

print('enter a number for the limit of fibonacci :')
number = int(input())
start = time.time()
u = fib(number)
print(u)
end = time.time()
print(end-start)
