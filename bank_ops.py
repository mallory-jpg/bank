# user operations: new account, check balance, transfer $, deposit, withdraw
# threading to make sure operations queue is intact
from bank_customers import USER_INFO
from bank_admin import Admin
import random
import threading
import logging

bal_lock = threading.Lock()

class BankAccount(Admin):

    def __init__(self, name, balance=0, account_id=[]):
        self.balance = balance
        self.account_id = account_id


    def new_account(self):
        for _ in range(9):
            self.account_id += str(random.randint(0, 9))
        print(f'Finished creating {self.account_id[-1]}')

        self.account_id.append(self.account_id)

        return f'Thank you for creating account number {self.account_id[-1]}'
    

    def check_balance(self):
        return f'Current Balance: {self.balance}'


    def withdraw(self, amount):
        bal_lock.acquire()
        amount = float(input('How much would you like to withdraw? Enter here: '))
        
        try:
            self.balance -= amount
        except:
            while self.balance < 0:
                print('Account balance cannot be negative')
                logging.warning('Negative balance')
            return
        finally:
            print(f'Withdrawing {amount} from {self.account_id}')
            bal_lock.release()
            return self.check_balance()


    def deposit(self, amount):
        bal_lock.acquire()
        amount = float(input('Deposit amount: ')) # must include cents
        self.balance += amount
        if amount > 10000:
            logging.info('Deposit amount exceeded')
            raise Exception('One-time deposits cannot exceed $10,000')
        else:
            print(f'Depositing {amount} into {self.account_id}')
            bal_lock.release()
        return self.check_balance()
    



