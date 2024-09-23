numbers = []
def squared():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    for number in numbers:
        print ("-", number, "squared equals: ", number * number)
    
    choice = input("Do you wish to try again? Y/N : ")
    if choice == "Y" or choice == "y":
        squared()
    elif choice == "N" or choice == "n":
        print ("goodbye, it was fun playing.")

squared()