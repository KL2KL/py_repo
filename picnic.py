allGuests = {'Alice' : {'apples' : 5, 'pretzels' : 12}, 'Bob' : {'ham sandwitches' : 3, 'apples' : 2}, 'Carol' : {'cups' : 3, 'apple pies' : 1}}

picnicItems = {'Sandwitches' : 4, 'Apples' : 12, 'Cups' : 4, 'Cookies' : 8000}

def totalBrought(guests, item):
  numBrought = 0
  for k, v in guests.items():
      numBrought = numBrought + v.get(item, 0)
  return numBrought

print('Number of things being brought:')
print('- apples      ' + str(totalBrought(allGuests, 'apples')))
print('- cups        ' + str(totalBrought(allGuests, 'cups')))
print('- cakes       ' + str(totalBrought(allGuests, 'cakes')))
print('- ham sandwitches ' + str(totalBrought(allGuests, 'ham sandwitches')))
print('- apple pies  ' + str(totalBrought(allGuests, 'apple pies')))

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)




