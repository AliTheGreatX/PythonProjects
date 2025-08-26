import random;
needle = random.randint(1,10);
chances = 3;
win = False;
print("Enter a number between 1 - 10");
while (chances > 0):
 input_ =input();
 if (input_ == str(needle)):
  win = True;
  print("You managed to guess the right number!! it's " + str(needle));
  break;
 elif input_ > str(needle): print("Go lower a bit");
 elif input_ < str(needle): print("Go higher a bit");
 chances -= 1;
if not win :   print("Wrong, Good Luck In The Next Times ):");
