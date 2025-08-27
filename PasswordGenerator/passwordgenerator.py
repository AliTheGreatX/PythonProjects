import random
# I used this password generator as a reference: https://www.lastpass.com/features/password-generator

#
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Get User Customization
pass_length = input("Enter the Length of the password 8-50 \n")
while(50< int(pass_length) <8 and pass_length.isnumeric == False):
    input("Make Sure the Length of the password is between 8-50 \n")
# Validation

def GetNewPassword():
    my_password = ""
    while len(my_password) < pass_length:
        random.randint()