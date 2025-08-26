import random
import time
player_streak = 0
com_streak = 0
choices = ["rock","paper","scissors"]

    
def game_loop(): 
  # Declare and Set variables  
  global player_streak
  global com_streak
  my_choice = ""
  comp_choice = ""
  
# validate input
  my_choice = str.lower(input("Choose: Rock - Paper - Scissors \n"))
  while(my_choice != choices[0]and my_choice != choices[1]and my_choice != choices[2]):
      my_choice = str.lower(input("Please make sure your choice is correct \n"))
  
  # shuffle computer choice
  comp_choice = random.choice(choices)

  # Tell the player what's happening (optional)
  time.sleep(1)
  print("You choose " + my_choice)
  time.sleep(1)
  print("Computer choose " + comp_choice)
  time.sleep(1)
  print("Deciding winner??")
  print("loading....")
  time.sleep(1)
  # check player case
  if(my_choice == "rock" and comp_choice == "scissors" or
     my_choice == "paper" and comp_choice == "rock" or
     my_choice == "scissors" and comp_choice == "paper"):
     player_streak +=1
     print("You win!")
  elif(my_choice == comp_choice):
          print("Tie! ")
  else:
      com_streak +=1
      print("You lose!")
  print("Your score is "+str(player_streak)+ " \ncomputer score is "+str(com_streak))
 

while(True):
  game_loop()