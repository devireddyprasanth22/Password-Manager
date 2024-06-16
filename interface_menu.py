# the interface that the user will see when this program is run
import maskpass 
from db import add_user, find_user, change_password, del_user, verify
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
    while True:
        choice = input(': ').upper()
        
        if choice in ['1', '2', '3', '4', 'Q']:
            return choice
        else:
            print("Invalid choice. Please enter a valid option (1-4 or Q).")

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
    else:
        password = password_generator()
        print(f'Your secure password for this application is {password}')
    add_user(username, email, password, application)
    print('Account created!')

def find_account():
    print('Please enter the email address: ')
    email = input()
    find_user(email)

def change_password(): 
    print('Please enter the email address: ')
    email = input()
    print('Please enter the username: ')
    username = input()
    old_pswd = maskpass.askpass(prompt="Please enter your old password:", mask="#")
    verify(email, username, old_pswd)
    new_pswd = maskpass.askpass(prompt="Please enter your new password:", mask="#")
    change_password(email, username, new_pswd)
    print('Password changed successfully!')

def del_account(): #-> del_user(email, username, password)
    print('Please enter the application name')
    application = input()
    print('Please enter the email address: ')
    email = input()
    print('Please enter the username: ')
    username = input()
    pswd =  maskpass.askpass(prompt="Please enter your password:", mask="#")
    del_user(email, username, pswd, application)
    print('Account deleted successfully')