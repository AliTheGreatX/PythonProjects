import random
# I used this password generator as a reference/inspiration: https://www.lastpass.com/features/password-generator

# Decleare sources
uAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lAlphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
symbols = "!@#$%^&*()_+-=~`|?/><.,:;'" 


# Get User Customization
pass_length = input("Enter the Length of the password 8-50 \n")

# Validation
while(50< int(pass_length) or int(pass_length) < 8 or pass_length.isnumeric == False):
 pass_length = input("Make Sure the Length of the password is between 8-50 \n")

pass_length = int(pass_length)
# Password Generation Proccess
def GetNewPassword():
    my_password = ""
    while len(my_password)< pass_length:
        which = random.randint(1,4)
        if():
         my_password+= uAlphabet[random.randint(0,len(my_password))]
    return my_password;
GetNewPassword()
# Output...
print("Your new password is \n" +GetNewPassword())