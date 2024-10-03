import users

print ('NON LOGGARE COME ADMIN, WORK IN PROGRESS!!!!!')
users.account_procedure()

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
        
def buy_item():
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
            break
    
if users.userOne['is_admin'] == True: # Dictates menu choices for administrators
    def admin_options():
        print('pizzocalabro QUESTO E UN PLACEHOLDER LEVALO DAL CAZZO QUANDO HAI FINITO')
else: # Dictates menu choices for basic users
    def user_options(): 
        print('hello ',users.userOne['username'],' What would you like to do?')
        print('Show inventory: 1')
        print('Buy something: 2')
        print('Show cart: 3')
        choice = int(input('Your choice: '))
        if choice == 1:
            show_inventory()
        elif choice == 2:
            print ('Great, let me show you the inventory to help you!')
            show_inventory()
            buy_item()
        elif choice == 3:
            print("here's how your cart is looking: ")
            show_cart()
        else:
            print