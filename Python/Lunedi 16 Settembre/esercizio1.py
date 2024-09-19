import random as r

def guessTheNumber():
    x = r.randint(1,10)
    exit = ""
    guess = 0
    while True:
        guess = int(input("Guess the number:"))
        if guess == x:
            print ("Congratulazions, you won.")
            break
        elif guess > x:
            print ("The number you guessed is bigger than the number to guess.")
        else:
            print ("The number you guessed is smaller than the number to guess.")

        exit = input("Want to keep trying or Restart? T/R")
        if exit == "t":
            print ("The number was:", x, ". Goodbye, it was good playing")
        elif exit == "r":
            print ("A new number to guess has been generated")
            vector()

def vector():
    guessTheNumber()

guessTheNumber()
