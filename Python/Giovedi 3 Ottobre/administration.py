import inventory

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
    