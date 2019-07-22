import copy

theBoard = {'1' : ' ', '2' : ' ', '3' : ' ', 
            '4' : ' ', '5' : ' ', '6' : ' ',
            '7' : ' ', '8' : ' ', '9' : ' '}

def printBoard(board):
  print(board['1'] + '|' + board['2'] + '|' + board['3'])
  print('-+-+-')
  print(board['4'] + '|' + board['5'] + '|' + board['6'])
  print('-+-+-')
  print(board['7'] + '|' + board['8'] + '|' + board['9'])

def judge():
  if (theBoard['1'] == theBoard['2'] == theBoard['3']) and (' ' not in theBoard['1']):
    return theBoard['1']
  elif theBoard['4'] == theBoard['5'] == theBoard['6'] and (' ' not in theBoard['4']):
    return theBoard['4']
  elif theBoard['7'] == theBoard['8'] == theBoard['9'] and (' ' not in theBoard['7']):
    return theBoard['7']
  elif theBoard['1'] == theBoard['4'] == theBoard['7'] and (' ' not in theBoard['1']):
    return theBoard['1']
  elif theBoard['2'] == theBoard['5'] == theBoard['8'] and (' ' not in theBoard['2']):
    return theBoard['2']
  elif theBoard['3'] == theBoard['6'] == theBoard['9'] and (' ' not in theBoard['3']):
    return theBoard['3']
  elif theBoard['1'] == theBoard['5'] == theBoard['9'] and (' ' not in theBoard['1']):
    return theBoard['1']
  elif theBoard['3'] == theBoard['5'] == theBoard['7'] and (' ' not in theBoard['3']):
    return theBoard['3']
  else:
    return 0

theBoardT = copy.copy(theBoard)
turn  = 'x'
counter = 9
printBoard(theBoard)
while counter > 0:
  print('Turn for ' + turn + '. Move on which space ?')
  move = input()
  if move not in theBoardT.keys():
    print('Number entered is not valid or location had been occupied, please select another one !')
    printBoard(theBoard)
    counter = counter + 1
  else:
    theBoard[move] = turn
    printBoard(theBoard)
    n = judge()
    if n != 0:
      print(turn + ' won the game !')
      break
    else:
      del(theBoardT[move])
    if turn == 'x':
      turn = 'o'
    else:
      turn = 'x'
  counter = counter - 1

if n == 0:
  print('Game is over without winner !')   

    
       
