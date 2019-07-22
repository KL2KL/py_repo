import sys, ast, os

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
    print('Usage: python3 my_chweight.py [date] (you must enter only one argument.)')
    sys.exit()

date = sys.argv[1]

if date in weights:
    print('Weight for ' + date + ' was ' + weights[date] + '.')
    print('What new weight do you wanna set to ?')
    new = input()
    if new != '':

        if new == weights[date]:
            print('You just entered the same value, so nothing changed!')
            sys.exit()

        weights[date] = new
        print('Weight for ' + date +' had been changed.')
        pass_file = open(path, 'w')
        pass_file.write(str(weights))
        pass_file.close()
    else:
        print('Nothing entered, database unchanged!')
else:
    print('There is no date : ' + date + ' found in database, Bye!')
   



