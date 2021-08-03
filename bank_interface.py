"""Connect to database & enter into bank simulation"""


import logging

from bank_ops import *
from bank_admin import *
from bank_customers import *
import storage


while __name__ == '__main__':
    # configure logs
    logging.basicConfig(filename='bank.log', filemode='w',
                format=f'%(asctime)s - %(self.name)s - %(levelname)s - %(message)s')
    
    print('Hello! Please wait while we connect...')

    # connect to db
    conn = storage.connect()
    
    # instantiate admin object
    admin = Admin()

    yes_no = input('Do you have an account with us? Y or N')
    if yes_no =='Y':
        admin.login()
    else:
        name = input('Alrighty then, let\'s create an account for you. What is your name?')
        user = Users(name.title)

        user.generate_uid()
        user.create_login()
        admin.login()
    
    account = BankAccount()

    print("""MAIN MENU:
            1~ Open a new account
            2~ Deposit
            3~ Withdraw
            4~ Check balance
            5~ View and modify account
            6~ Log off
        """)
    response = input('Please choose an option (1-6): ')

    if response == '1':
        account.new_account()
    elif response == '2':
        account.deposit()
    elif response == '3':
        account.withdraw()
    elif response == '4':
        account.check_balance()
    elif response == '5':
        choice = input('Choose [1] Create new username [2] Create new password [3] View account information')
        if choice == '1':
            admin.new_user()
            admin.login()
        elif choice == '2':
            admin.new_pw()
            admin.login()
        elif choice == '3':
            print("""User ID: {self.uid}
                    {self.account}
            """)
        else:
            print('Invalid choice. Please try again.')
    elif response == '6':
        storage.connect.close()
        print('Goodbye')
    else:
        print('Invalid choice. Please try again.')

        
    
    


# start of the program

