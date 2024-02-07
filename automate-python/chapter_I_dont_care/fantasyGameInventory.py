stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print("Inventory: ")


def displayInventory(inventory):
    totalItem = 0
    for k, v in inventory.items():
        print(k, v)
        totalItem += v
    print("Total number of itenms:", totalItem)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1;

displayInventory(stuff)
addToInventory(inventory=stuff, addedItems= dragonLoot)
displayInventory(stuff)
