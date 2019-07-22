import sys, ast, os

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
    print('Usage: python3 ch_password.py [account] (you must enter only one argument.)')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    print('Password for ' + account + ' was ' + passwords[account] + '.')
    print('What new password do you wanna set to ?')
    new = input()
    if new != '':
        passwords[account] = new
        print('Password for ' + account +' had been changed.')
        pass_file = open(path, 'w')
        pass_file.write(str(passwords))
        pass_file.close()
    else:
        print('Nothing entered, database unchanged!')
else:
    print('There is no account : ' + account + ' found in database, Bye!')
   


