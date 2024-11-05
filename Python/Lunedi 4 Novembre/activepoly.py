class Flower:
    flower_type = None
    def __init__(self, stalk, petals):
        self.stalk = stalk
        self.petals = petals
    
    def getinfo(self):
        self.stalk = input('Insert the lenght of the stalk: ')
        self.petals = input('Insert the color of the petals: ')
        
    def printinfo(self):
        print(f'The flower is a {self.flower_type}, the stalk is {self.stalk}cm long and the petals are {self.petals}')
    
class Rose(Flower):
    flower_type = 'Rose'
    def __init__(self, stalk, petals, season):
        super().__init__(stalk, petals)
        self.season = season
        
    def getinfo(self):
        self.season = 'Spring/Summer'
        self.stalk = int(input('Insert the lenght of the stalk: '))
        self.petals = input('Insert the color of the petals: ')
        
    def printinfo(self):
        print(f'The {self.flower_type} grows mostly during {self.season}, the stalk is {self.stalk}cm long and the petals are {self.petals}')

class Tulip(Flower):
    flower_type = 'Tulip'
    def __init__(self, stalk, petals, season):
        super().__init__(stalk, petals)
        self.season = season
        
    def getinfo(self):
        self.season = 'Spring'
        self.stalk = int(input('Insert the lenght of the stalk: '))
        self.petals = input('Insert the color of the petals: ')
        
    def printinfo(self):
        print(f'The {self.flower_type} grows mostly during {self.season}, the stalk is {self.stalk}cm long and the petals are {self.petals}')

def createflower(flower):
    flo_ty = input("what type of flower are you trying to insert? ")
    if flo_ty == flower.flower_type:
        flower.getinfo()
        flower.printinfo()
    else:
        print ('You are trying to insert the wrong flower type')
        
rose = Rose('','','')

createflower(rose)