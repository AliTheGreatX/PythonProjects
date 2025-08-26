import random;
needle = random.randint(1,10);
chances = 3;
win = False;
while (chances > 0):
 input_ =input("Enter a number between 1 - 10 \n");
 if (input_ == needle):
  win = True;
  print("You managed to guess the right number!! it's " & input_);
  break;
 chances -= 1;
if not win :   print("You managed to guess the right number!! it's " & input_);
