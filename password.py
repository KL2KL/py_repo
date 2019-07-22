import sys, pyperclip, ast, os

path = '/Applications/py_local/db.txt'
if os.path.isfile(path):
    pass_file = open(path, 'r+')
else:
    pass_file = open(path, 'w')
    pass_file.write('{}')
    pass_file = open(path, 'r+')

x = pass_file.read()
passwords = ast.literal_eval(x)
pass_file.close()

if len(sys.argv) != 2:
    print('Usage: python3 password.py [account] (you must enter only one argument.)')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account : ' + account + '\n' + 'Enter the password for ' + account + ' :')
    word = input()
    if word != '':
        passwords[account] = word
        print('Database updated')
        pass_file = open(path, 'r+')
        pass_file.write(str(passwords))
        pass_file.close()
    else:
        print('Nothing entered, Please try again!')
    



