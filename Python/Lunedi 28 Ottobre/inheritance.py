class Car:
    engineType = ''
    def __init__(self, make, model, engineType):
        self.make = make
        self.model = model
        self.engineType = engineType
    def show_info(self):
        print (f"This car is a {self.make} {self.model}") 
    def engine(self):
        pass
    
class Ferrari(Car):
    def __init__(self, make, model, engineType, horsepower):
        super().__init__(make, model, engineType)
        self.horsepower = horsepower
    def show_info(self):
        print (f"This car is a {self.make} {self.model} and it has just under {self.horsepower} hp")
    def engine(self):
        print (f"this car is petrol and has a {self.engineType}")
        
class Pagani(Car):
    fun_fact = "it's one of the best selling cars Pagani has ever built, what a wonderful car!"
    def __init__(self, make, model, engineType):
        super().__init__(make, model, engineType)
    def show_info(self):
        print (f"This car is a {self.make} {self.model}, {self.fun_fact}")
    def engine(self):
        print (f"this car is petrol and has a {self.engineType}")
        
class Bugatti(Car):
    def __init__(self, make, model, engineType):
        super().__init__(make, model, engineType)  
    def engine(self):
        print (f"this car is petrol and is rocking the brand new {self.engineType} engine!")
        
car1 = Ferrari('Ferrari','F250','LeMans derived Twin-Turbo V6', 1200)
car2 = Pagani('Pagani','Huayra','Twin-Turbo V12 ')
car3 = Bugatti('Bugatti','Tourbillon','Quad-Turbo V16')

car1.show_info()
car1.engine()
print (' ')
car2.show_info()
car2.engine()
print (' ')
car3.show_info()
car3.engine()
