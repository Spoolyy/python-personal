class Automobile:
    number_of_tires = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def print_info(self):
        print('the car is a', self.make, self.model)
        print('the car has', self.number_of_tires,' tires')

auto1 = Automobile("Nissan", "Skyline")
auto2 = Automobile("Ferrari", "F40")

auto1.number_of_tires = 6

auto1.print_info()
auto2.print_info()
