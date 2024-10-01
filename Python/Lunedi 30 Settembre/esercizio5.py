numbers = []
def user_name():
    name = input("Please insert your name: ")
    print (name)
    
def smallest_divisor(num):
    if num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                return i
    return None

def is_prime():
    while True:
        number = int(input("Please insert a number: "))
        numbers.append(number)

        if number > 1:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    smallest_div = i 
                    break
            
            if is_prime:
                print(number, "is a prime number.")
            else:
                print(number, "is not a prime number. The smallest divisor is: ", smallest_div)
        else:
            print(number, "is not a prime number.")

        choice = input("Press Enter to repeat or type STOP to exit the program: ").lower()
        if choice == "stop":
            print("Thanks for using my program")
            break

def show_divisors():
    print("Here is your list of numbers and their smallest divisors:")
    for num in numbers:
        divisor = smallest_divisor(num)
        if divisor:
            print(num, "Smallest divisor is: ", divisor)
        else:
            print(num, "No divisor (number is 1 or less)")
            
def procedure():
    user_name()
    is_prime()
    show_divisors()

procedure()