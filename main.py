# create a master password encryption key and handle encryption and decryption of data here
from interface_menu import *
from reader import get_key
from encrypt import generate_key
def main():
    pswd =  maskpass.askpass(prompt="Please enter your password for masteradmin:", mask="#")
    key = get_key()
    if key == pswd:
        print("Success!")
    else:
        print("Incorrect")
        exit()
    while True:
        menu = options()
        
        if menu == '1':
            add_account()
        elif menu == '2':
            find_account()
        elif menu == '3':
            change_password()
        elif menu == '4':
            del_account()
        elif menu == '5':
            all_accounts()
        elif menu.upper() == 'Q':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    
    exit()


if __name__ == "__main__":
    generate_key()
    main()