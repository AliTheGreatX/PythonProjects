import random;
import os;
needle = random.randint(1,10);
chances = 3;
win = False;
while (chances > 0):
 input_ =input("Enter a number between 1 - 10 \n");
 if (input_ == str(needle)):
  win = True;
  print("You managed to guess the right number!! it's " + str(needle));
  break;
 os.system("cls");
 print("Try again");
 chances -= 1;
if not win :   print("Wrong, Good Luck In The Next Times ):");
