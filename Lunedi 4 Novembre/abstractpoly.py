from abc import ABC, abstractmethod

class data(ABC):
    @abstractmethod
    def getData():
        pass
    
class Login(data):
    username = None
    __password = None
    is_admin = False
    admin_key = '123abc'
    
    def __setpassword(self, password):
        self.__password = password
    
    def getPassword(self):
        password = self.__password
        return password
    
    def getData(self):
        if self.is_admin:
            print (f'username: {self.username} | password: {self.getPassword()} | You are admin')
        else:
            print (f'username: {self.username} | password: {self.getPassword()}')
            
    def __loginSuccessfull(self):
        print ("you're a champ ;)")
    
    def registerUser(self):
        print ('Register below: ')
        print ('')
        user_input = input('Set your username: ')
        pw_input = input('Set your password: ')
        print ('')
        self.username = user_input
        self.__setpassword(pw_input)
        while True:
            admin_choice = input('Would you like to register as administrator? y/n: ').lower()
            if admin_choice not in ['y', 'n']:
                print("Please enter 'y' or 'n'")
                continue
            if admin_choice == 'y':
                while True:
                    admin_key_input = input('Please insert your admin key to register as Administrator: ')
                    if admin_key_input == self.admin_key:
                        self.is_admin = True
                        print('Administrator register process complete')
                        break
                    elif admin_key_input == 'exit':
                        break
                    else:
                        print('Wrong administrator key, please try again or type "exit" to cancel')
            else:
                print('Register process complete')
                break
            break
                
    def loginUser(self):
        while True:
            if not self.username:
                self.registerUser()
            else:
                print ('Login Below: (type "exit" to abort login)')
                print ('')
                username = input('insert your username: ')
                password = input('insert your password: ')
                print ('')
                if username == self.username and password == self.getPassword():
                    if self.is_admin:
                        print ('Successfully logged in as administrator')
                    else:
                        print ('Successfully logged in')
                    self.__loginSuccessfull()
                    break
                else:
                    print ('Wrong credentials, try again')
                    if username == 'exit':
                        print ('Login procedure cancelled')
                        break

def loginprocedure(user):
    user.loginUser()
    user.getData()

pippo = Login()

loginprocedure(pippo)

                
            
        
    
    