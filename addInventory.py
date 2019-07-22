def addToInventory(invent, addItems):
    for i in range(len(addItems)):
        invent.setdefault(addItems[i], 0)
        invent[addItems[i]] = invent[addItems[i]] + 1

    return invent

def displayInventory(inventory):
    print('Inventory :')
    item_total = 0
    for k, v in inventory.items():
        print(k + ' ' + str(v))
        item_total = item_total + v
        
    print('Total number of items: ' + str(item_total))

inv = {'gold coin' : 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

