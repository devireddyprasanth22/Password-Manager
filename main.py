# create a master password encryption key and handle encryption and decryption of data here
import maskpass  # importing maskpass library

pwd = maskpass.askpass(prompt="Password:", mask="#")