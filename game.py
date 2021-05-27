

import random


print("Welcome USER_NAME to Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

#print(user_choice)
print("USER CHOICE: ", user_choice)


# validate input so that it is only one of the expected values
# will stop program before it tries to do anything else
# will have it make user run it again


if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID, KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit () 

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ", computer_choice)

#condition checks for winner
if (user_choice == computer_choice):
    print ("You tied this round")

elif ((user_choice == "rock") and computer_choice == "paper"):
   print ("Paper beats rock, sorry you lose!")

elif ((user_choice == "rock") and computer_choice == "scissors"):
   print ("Rock beats scissors, great you win!")

elif ((user_choice == "paper") and computer_choice == "rock"):
  print ("Paper beats rock, great you win!")

elif ((user_choice == "paper") and computer_choice == "scissors"):
   print ("Scissors beats paper, sorry you lose!")   

elif ((user_choice == "scissors") and computer_choice == "rock"):
   print ("Rock beats scissors, sorry you lose!")

elif ((user_choice == "scissors") and computer_choice == "paper"):
   print ("Scissors beats paper, great you win!")     
    

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")

exit ()