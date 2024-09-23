userOne = {
    "id": None,
    "username": None,
    "password": None
}

def procedure():
    if userOne.get("id"):
        login()
        print(" ")
    else:
        register()
        print(" ")

def register():
    print("it appears you don't have an account, create one below:")
    username = input("choose your username: ")
    password = input("choose a password: ")
    userOne["username"] = username
    userOne["password"] = password
    userOne["id"] = 0
    userOne["id"] += 1
    print(" ")
    choice = input("do you wish to log in or erase your account?")
    if choice == "login":
        login()
    elif choice == "erase":
        userOne["id"] = None
        userOne["username"] = None
        userOne["password"] = None


def login():
    print("Please insert your credentials below:")
    print(" ")
    username = input("insert your username: ")
    password = input("insert your password: ")
    if username == userOne["username"] and password == userOne["password"]:
        print ("you have successfully logged in")

procedure()