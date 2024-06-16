# create a master password encryption key and handle encryption and decryption of data here
from interface_menu import *
from reader import get_key
def main():
    pswd =  maskpass.askpass(prompt="Please enter your password for masteradmin:", mask="#")
    key = get_key()
    if key == pswd:
        print("Success!")
    else:
        print("Incorrect")
        exit()
    menu = options()
    while True:
        match menu:
            case 1:
                add_account()
            case 2:
                find_account()
            case 3:
                change_password()
            case 4:
                del_account()
            case "Q":
                exit()