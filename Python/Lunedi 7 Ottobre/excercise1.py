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
        
examplecar = Cars('Nissan', 'Skyline', 1999)
examplecar.printinfo()

def create_new_car():
    car1 = Cars('','','')
    car1.getinfo()
    car1.printinfo()

create_new_car()