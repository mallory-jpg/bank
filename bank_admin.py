# bank account administration: welcome, login, operations, set pw, cancel account
# from bank_customers import User

from bank_customers import Users, USER_INFO 
# from bank_customers import save_user_info

BANK_NAME = 'No Cap'
# USER_INFO = {}

class Admin(Users):
    def __init__(self, username='admin', password='0000'):
        super().__init__(self.name, self.uid, self.account)
        self.username = username 
        self.password = password
        self._login = True
        print('Welcome, {self.username.split('')}')
        
        # USER_INFO[self.name] = {'password': self.password}

    def new_user(self, new_user=None):
        new_user = input('Enter new username: ')
        self.username = new_user
        print('Username updated.')
        self.save_user_info()
        return self.username
    
    def new_pw(self, new_password=None):
        try:
            new_password = input('Enter new password: ')
        except:
            pass
        finally:
            self.password = new_password
            print('Password updated.')
        self.save_user_info()
        return self.password

    def login(self, username=None, pw=None):
        attempts = 0
        if not self._login:
            username = input('Username please : ')
            pw = input('Password please: ')
        if username == self.username and pw == self.password:
            return True
        else:
            while attempts <= 3:
                attempts += 1
                # LOG
                print('Incorrect login information. Please try again.')
            else:
                print('Please reset password')
                self.new_pw()
            return

    def lock_account(self):
         pass
    
  