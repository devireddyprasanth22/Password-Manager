# create a master password encryption key and handle encryption and decryption of data here
from interface_menu import *

def main():
    pswd =  maskpass.askpass(prompt="Please enter your password for masteradmin:", mask="#")