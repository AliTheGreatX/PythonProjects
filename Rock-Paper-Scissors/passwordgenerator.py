import random
# I used this password generator as a reference: https://www.lastpass.com/features/password-generator

#
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Get User Customization
pass_length = input("Enter the Length of the password 8-50")

# Validation

def GetNewPassword():
    my_password = ""
    while len(my_password) < pass_length:
        random.randint()