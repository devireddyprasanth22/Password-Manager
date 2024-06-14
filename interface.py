# the interface that the user will see when this program is run
import maskpass 
from db import add_user, find_user, change_password, del_user
from password_gen import password_generator

yes = {'yes','y', 'ye', ''}
no = {'no','n'}
def options():
    print(('-'*6) + 'Menu'+ ('-' *6))
    print('1. Add new account credentials')
    print('2. Find account associated to email')
    print('3. Change password for account')
    print('4. Delete account credentials')
    print('Q. Exit')
    return input(': ')

def add_account(): #-> add_user from db
    print('Name of application: ')
    application = input()
    print('Email for this application: ')
    email = input()
    print('Username for this application')
    username = input()
    print('Do you already have a password for this application [Y,n]: ')
    choice = input()
    if choice in yes:
        password = maskpass.askpass(prompt="Please enter your password:", mask="#")
    elif choice in no:
        password = password_generator()
        print(f'Your secure password for this application is {password}')
    add_user(username, email, password, application)
    print('Account created!')

def find_account() #-> find_usr(email) from db
    print('Please enter the email address: ')
    email = input()
# def change_password() -> change_password(email, username, new password)
# def del_account -> del_user(email, username, password)