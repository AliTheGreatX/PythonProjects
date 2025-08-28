import random
import string
# I used this password generator as a reference/inspiration: https://www.lastpass.com/features/password-generator

# Get User Customization
pass_length = input("Enter the Length of the password 8-50 \n")

# Validation
while(50< int(pass_length) or int(pass_length) < 8 or pass_length.isnumeric == False):
 pass_length = input("Make Sure the Length of the password is between 8-50 \n")

# Check if the answer is non numeric value
# if(pass_length.isnumeric == False):
#     raise ValueError("Make sure it's a number!")
# change it to an integer
pass_length = int(pass_length)

hasSymbols = str.lower(input("Does it has symbols?? y/n\n"))
if(hasSymbols != "y" and hasSymbols !="n"): raise ValueError("Sorry it shold be yes or no input")
hasNumbers=  str.lower(input("Does it has Numbers?? y/n\n"))
if(hasNumbers != "y" and hasNumbers !="n"): raise ValueError("Sorry it shold be yes or no input")
hasLowerCase=  str.lower(input("Does it has LowerCase?? y/n\n"))
if(hasLowerCase != "y" and hasLowerCase !="n"): raise ValueError("Sorry it shold be yes or no input")
hasUpperCase=  str.lower(input("Does it has UpperCase?? y/n\n"))
if(hasUpperCase != "y" and hasUpperCase !="n"): raise ValueError("Sorry it shold be yes or no input")
# Password Generation Proccess
def GetNewPassword():
    my_password = ""
    nmbers = "0123456789"
    while len(my_password)< pass_length:
        which = random.randint(1,4)
        if(hasUpperCase == "y" and which == 1):
         my_password+= string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase))]
        if(hasLowerCase == "y"and which == 2):
         my_password+= string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase))]
        if(hasSymbols == "y"and which ==3):
         my_password+= string.punctuation[random.randint(0,len(string.punctuation))]
        if(hasNumbers == "y"and which == 4):
         my_password+= nmbers[random.randint(0,len(nmbers))]
    return my_password
GetNewPassword()
# Output...
print("Your new password is \n" +GetNewPassword())