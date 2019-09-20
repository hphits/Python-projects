def addtoinventory(inventory,addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return(inventory)

def displayInventory(inventory):
    print('Inventory: ')
    total = 0
    l = 0
    for k,v in inventory.items():
        print(k,v)
        total = total + v
        l = l + 1
    print('Total number of items are: ' + str(l) + ' and total quantity: ' + str(total))


inv = {'gold coin' : 42, 'rope': 1}
dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addtoinventory(inv, dragonloot)
displayInventory(inv)
