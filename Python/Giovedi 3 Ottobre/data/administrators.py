import inventory
import users

def admin_menu():
    print('hello admin: ',users.userOne['username'],'. What would you like to do?')
    print('Show inventory: 1')
    print('Edit Inventory: 2')
    print('Show total earnings: 3')
    while True:
        choice = int(input('Your choice: '))
        if choice == 1:
            inventory.show_inventory()
            break
        elif choice == 2:
            print ('Great, let me show you the inventory to help you!')
            inventory.show_inventory()
            add_item()
            break
        elif choice == 3:
            print("here's how your cart is looking: ")
            inventory.show_cart()
            break
        else:
            print('You have selected an invalid option.')

def add_item():
    new_item = [
        
    ]
    sorting_id = len(inventory.inventory)-1
    new_item.append(sorting_id)
    while True:
        item_id = input('Insert a 4 character item ID: ')
        if len(item_id) == 4:
          new_item.append(item_id)
          break
        else:
            print('your ID is either too long or too short. 4 Character min/max. : ')
    description = input('Insert an item description: ')
    new_item.append(description)
    price = float(input('Insert a price: '))
    new_item.append(price)
    pieces = int(input('Insert the stock amount: '))
    new_item.append(pieces)
    inventory.inventory.append(new_item)
        
    choice = input('Would you like to add another item? y/n').lower()
    if choice == 'y':
        add_item()
    elif choice == 'n':
        print('All item/s added successfully')
    else:
        input('insert a valid option')
