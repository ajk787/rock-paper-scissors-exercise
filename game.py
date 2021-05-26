


print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors':")

#print(user_choice)
print("USER CHOICE: ", user_choice)


# validate input so that it is only one of the expected values
# will stop program before it tries to do anything else
# will have it make user run it again




if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID, KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
exit()

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")