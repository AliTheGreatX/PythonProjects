import random
import string
# I used this password generator as a reference/inspiration: https://www.lastpass.com/features/password-generator

# Get User Customization
pass_length = input("Enter the Length of the password 8-50 \n")
hasSymbols = str.lower(input("Does it has symbols?? y/n\n"))
if(hasSymbols != "y" and hasSymbols !="n"): raise ValueError("Sorry it shold be yes or no input")
hasNumbers=  str.lower(input("Does it has Numbers?? y/n\n"))
if(hasNumbers != "y" and hasNumbers !="n"): raise ValueError("Sorry it shold be yes or no input")
hasLowerCase=  str.lower(input("Does it has LowerCase?? y/n\n"))
if(hasLowerCase != "y" and hasLowerCase !="n"): raise ValueError("Sorry it shold be yes or no input")
hasUpperCase=  str.lower(input("Does it has UpperCase?? y/n\n"))
if(hasUpperCase != "y" and hasUpperCase !="n"): raise ValueError("Sorry it shold be yes or no input")
# Validation
while(50< int(pass_length) or int(pass_length) < 8 or pass_length.isnumeric == False):
 pass_length = input("Make Sure the Length of the password is between 8-50 \n")

pass_length = int(pass_length)
# Password Generation Proccess
def GetNewPassword():
    my_password = ""
    while len(my_password)< pass_length:
        allCharacters = ""
        if(hasUpperCase):
            allCharacters += string.ascii_uppercase
        if(hasLowerCase):
            allCharacters += string.ascii_lowercase
        if(hasSymbols):
            allCharacters += string.punctuation
        if(hasNumbers):
            allCharacters += "123456789"
        my_password+= allCharacters[random.randint(0,len(allCharacters))]
    return my_password
GetNewPassword()
# Output...
print("Your new password is \n" +GetNewPassword())