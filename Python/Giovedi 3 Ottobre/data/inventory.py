inventory = [
    ['ID','Item ID', 'Descrizione', 'Prezzo', 'Pezzi in Stock'],
    [1,'mr19', 'Maglietta Rossa', 19.99, 100],
    [2,'pb24', 'Pantalone Blu', 24.99, 80],
    [3,'bcb9', 'Bundle calzini Bianchi', 9.99, 250],
    [4,'gi20', 'Giacca Invernale', 199.99, 50],
    [5,'tLE9', 'Tuxedo Limited edition', 4999.99, 10],
]

user_cart = [
    
]

user_purchases = [
    
]

def show_inventory():
    for item in inventory:
        print ('| ID: ',item[0],'Identificativo: ',item[1],'| Descrizione: ',item[2],'| Prezzo: $',item[3],'| in stock: ',item[4],'pz.')
        
def show_cart():
    for item in user_cart:
        print ('Identificativo: ',item[1],'| Descrizione: ',item[2],'| Prezzo: $',item[3],'| in stock: ',item[4],'pz.')
        
def add_to_cart():
    print('choose the item based on their ID: ')
    while True:
        choice = int(input('ID: '))
        if choice > len(inventory):
            print('error: item does not exist')
        elif choice == 0:
            print('error, enter a valid item ID')
        else:
            user_cart.insert(inventory[choice])
            print('Great, item added to your cart')
            choice = input('Would you like to add another item? y/n').lower()
            if choice == 'y':
                add_to_cart()
            elif choice == 'n':
                break
            
            
            