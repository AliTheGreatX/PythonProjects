import math

while(True):
    x = int(input("Enter the first number\n"))
    y = int(input("Enter the second number\n"))
    print("Choose an operation: ")
    print(" 1-Sum \n 2-Subtract \n 3-Multiply \n 4-Divide")
    operation =  input("What do you want to do? Please Select Numbers for the operation (e.g 1 to perform sum)")
    if(operation=="1"):
     z = x+y
    elif (operation=="2"):
     z = x-y
    elif (operation=="3"):
     z = x*y
    elif (operation=="4"):
     try:
        z = x/y
     except ZeroDivisionError:
        z = 0
    else:
        print("Thanks for using my app")
        break
    print("the results of the operation is equal to: "+ str(z))
    