fixedcredentials = {
    "administrationKey": 'admin99'
}

userOne = {
    "user_id": None,
    "admin_id": None,
    "username": None,
    "password": None,
    "is_admin" : False,
}

def account_procedure():
    if userOne.get("user_id") or userOne.get("admin_id"):
        login()
        print(" ")
    else:
        print("it appears you don't have an account, create one below: ")
        choice = input("Are you registering as user or as an administrator? U/A").lower()
        if choice == 'u':
            register_user()
        elif choice == 'a':
            register_admin()
   
def register_user():
    print("register as user below: ")
    username = input("choose your username: ")
    password = input("choose a password: ")
    userOne["user_id"] = 0
    userOne["user_id"] += 1
    userOne["username"] = username
    userOne["password"] = password
    print(" ")
    login()
        
def register_admin():
    admin_key = input("Please write down the administrator key you've been provided: ")
    if admin_key != fixedcredentials["administrationKey"]:
        print('ERROR: the administrator key you entered is not valid, try again')     
        register_admin()
    else:
        print("Administrator key accepted, enter your credentials below: ")
        username = input("choose your username: ")
        password = input("choose a password: ")
        userOne["admin_id"] = 0
        userOne["admin_id"] += 1
        userOne["username"] = username
        userOne["password"] = password
        userOne["is_admin"] = True
    print(" ")
    login()


def login():
    print("login.")
    print("Please insert your credentials below:")
    print(" ")
    username = input("insert your username: ")
    password = input("insert your password: ")
    if username == userOne["username"] and password == userOne["password"]:
        if not(userOne.get("user_id")) and userOne.get("admin_id"):
            print ("Hello ",username,", you have successfully logged in, your admin id is: ",userOne['admin_id'])
        else:
            print ("Hello ",username,", you have successfully logged in")