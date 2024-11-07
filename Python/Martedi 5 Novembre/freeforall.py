import random

class User:
    def __init__(self, name, password, score):
        self.name = name
        self.__password = password
        self.__score = score
        
    def GET_Score(self):
        score = self.__score
        return score
    
    def SET_Score(self, score):
        self.__score = score
        
    def GET_pw(self):
        pw = self.__password
        return pw
    
    def SET_pw(self, pw):
        self.__password = pw
        
    def SET_Name(self, name):
        self.name = name
        
class Application(User):
    
    UserList = [
        User('Alessio', 'pass1', 0),
        User('Mirko', 'pass2', 0),
        User('Davide', 'pass3', 0),
        User('Emanuele', 'pass4', 0)
    ]
    is_logged = False
    current_user = None
    
    def login(self):
        print(f'Login below:')
        while True:
            name = input('Insert Name: ')
            pw = input('Insert Password: ')
            for user in self.UserList:
                if name == user.name and pw == user.GET_pw():
                    print (f'welcome {user.name}, your current score is {user.score}')
                    self.is_logged = True
                    self.current_user = user
                    break
                print (f'error, wrong credentials.')
    
    def game(self):
        while True:
            if not self.is_logged:
                self.login()
            else:
                user = self.current_user

            while True:
                firstnumber = random.randint(1, 100)
                secondnumber = random.randint(1, 100)
                result = firstnumber + secondnumber
                response = int(input(f"What's {firstnumber} + {secondnumber}? "))
                
                if response == result:
                    print("Correct!")
                    user.score += 3
                    print(f"Your new score is {user.score}")
                elif response == "exit":
                    self.is_logged = False
                    break
                else:
                    print("Incorrect, try again.")
                    user.score -= 1
                    print(f"Your new score is {user.score}")
                
    
            
        
