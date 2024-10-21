from data import Analyzer

def getnumbers(): 
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    return numbers