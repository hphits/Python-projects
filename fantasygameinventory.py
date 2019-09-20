
stuff = {'Arrow': 12, 'Gold Chain': 42, 'Rope': 1, 'Torch': 6, 'Dagger': 1}

def displayInventory(inventory):
    print('Inventory: ')
    total = 0
    l = 0
    for k,v in inventory.items():
        print(k,v)
        total = total + v
        l = l + 1
    print('Total number of items are: ' + str(l) + ' and total quantity: ' + str(total))


displayInventory(stuff)
