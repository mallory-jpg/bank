# load & save user info
import random

# all users?
USER_INFO = {}

class Users:

    def __init__(self, name, uid='', username='', password='', account={}):
        self.account = account
        self.name = name
        self.uid = uid
        self.username = username
        self.password = password
        self._login = None

        # USER_INFO[self.name] = {'uid': self.uid}
       
# store user info 
    def save_user_info(self):
        print('Saving...')
        for key, value in self.account.items():
            setattr(self, key, value)
        print('Saved.')
        
    def generate_uid(self, length=10):
            for _ in range(length):
                self.uid += str(random.randint(0,9))
            self.save_user_info()
            return self.uid
    
    def create_login(self):
            while True:
                self.password = input('Create password: ')
                self.confirm = input('Confirm password: ')
                
                if self.password == self.confirm:
                    break
                self.save_user_info()



