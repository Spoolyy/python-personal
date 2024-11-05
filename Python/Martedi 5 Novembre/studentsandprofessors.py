class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def GET_NAME(self):
        name = self.__name
        return name
    
    def GET_AGE(self):
        age = self.__age
        return age
    
    def SET_NAME(self, name):
        self.__name = name
        
    def SET_AGE(self, age):
        self.__age = age
    
    def introduction(self):
        print (f'hello my name is {self.GET_NAME()} and i am {self.GET_AGE()} years old, nice to meet you')

class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades
    
    def average_grades(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def introduction(self):
        print (f'hello my name is {self.GET_NAME()} and i am {self.GET_AGE()} years old, nice to meet you')
        print (f'My grades are {self.grades} and the average is {self.average_grades()}')

class Professor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def introduction(self):
        print (f'hello my name is {self.GET_NAME()} and i am {self.GET_AGE()} years old, nice to meet you')
        print (f'I teach {self.subject}')
        
def personintroduction(person):
    person.introduction()
    
def change_age(person):
    age = int(input(f'Modify your age: (Your current age is {person.GET_AGE()}) '))
    person.SET_AGE(age)
    print (person.GET_AGE())
    
def change_name(person):
    name = input(f'Modify your name: (Your current name is {person.GET_NAME()}) ')
    person.SET_NAME(name)
    print (person.GET_NAME())

        
p1 = Student('Alessio', 25, [10,2,4,5,6,7])
p2 = Professor('Mirko', 29, 'Object Oriented Programming')

personintroduction(p1)
print ('')
personintroduction(p2)
print ('')
change_name(p1)
change_age(p1)
print ('')
personintroduction(p1)

    
        