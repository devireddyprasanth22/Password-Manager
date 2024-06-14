# the interface that the user will see when this program is run

def options():
    print(('-'*6) + 'Menu'+ ('-' *6))
    print('1. Add new account credentials')
    print('2. Find account associated to email')
    print('3. Change password for account')
    print('4. Delete account credentials')
    print('Q. Exit')
    return input(': ')

# def add_account() -> add_user from db
# def find_account() -> find_usr(email) from db
# def change_password() -> change_password(email, username, new password)
# def del_account -> del_user(email, username, password)