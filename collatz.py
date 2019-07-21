def collatz():
    print('enter an original value for the collatz sequence :')
    number = int(input())
    while True:
        if number == 1:
            break
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        print(int(number))
collatz()

