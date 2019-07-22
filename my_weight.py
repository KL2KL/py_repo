import sys, ast, os
import matplotlib.pyplot as plt

path = 'weights.txt'

if os.path.isfile(path):
    pass_file = open(path, 'r+')

else:
    pass_file = open(path, 'w')
    pass_file.write('{}')
    pass_file = open(path, 'r+')

x = pass_file.read()
weights = ast.literal_eval(x)
pass_file.close()

if len(sys.argv) != 2:
    print('Usage: python3 my_weight.py [date] (you must enter only one argument.)')
    sys.exit()

date = sys.argv[1]

if date in weights:
    records_value = list(weights.values())
    records_key = list(weights.keys())
    n = records_key.index(date)

    for i in range(len(records_value)):
        records_value[i] = float(records_value[i])

    v = records_value[0:n+1]
    print(v)
    plt.plot(v, 'ro')
    plt.grid()
    plt.savefig(date + 'weight.pdf')
    plt.show()
    
else:
    print('There is no date : ' + date + '\n' + 'Enter the weight for ' + date + ' :')
    word = input()

    if word != '':
        weights[date] = word
        print('Database updated')
        pass_file = open(path, 'r+')
        weights = dict(sorted(weights.items()))
        pass_file.write(str(weights))
        pass_file.close()

    else:
        print('Nothing entered, Please try again!')
    




