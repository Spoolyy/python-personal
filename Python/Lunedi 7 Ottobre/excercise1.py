class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def getinfo(self):
        self.make = input('Insert a make: ')
        self.model = input('insert a model: ')
        self.year = int(input('insert the production year: '))
        
    def printinfo(self):
        print('the car is a', self.year, self.make, self.model)
        
    def __str__(self):
        return f"Car(Make: {self.make}, Model: {self.model}, Year: {self.year})"
        
examplecar = Cars('Nissan', 'Skyline', 1999)
examplecar.printinfo()

CarsArray = [
    
]

def create_new_car():
    while True:
        newcar = Cars('','','')
        newcar.getinfo()
        CarsArray.append(newcar)
        choice = input('do you wish exit or continue adding cars? ').lower()
        if choice == 'exit':
            for Car in CarsArray:
                print(Car)
            break
create_new_car()