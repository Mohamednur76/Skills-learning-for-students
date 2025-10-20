
#---this is a simple rock paper scissors game---#

import random
print("Welcome to Rock, Paper, Scissors!")

#--Player makes a choice and computer makes a choice--#
computer_choice = random.choice(['rock', 'paper', 'scissors'])
player_choice = input("enter rock, paper, or scissors: ").lower()

while player_choice not in ['rock', 'paper', 'scissors']:
    player_choice = input("Invalid choice. Watch the spellings too. Please enter rock, paper, or scissors: ").lower()
    player_choice = input("enter rock, paper, or scissors: ").lower()


#--Game's Logic--#
if player_choice == computer_choice:
    print(f"Both chose {player_choice}, so its a tie")
elif (player_choice == 'rock' and computer_choice == 'paper') or player_choice == 'paper' and computer_choice == 'scissors' or player_choice == 'scissors' and computer_choice == 'rock':
    print(f"Computer chose {computer_choice}. You lose!")
else:
    print(f"Computer chose {computer_choice}. You win!")
print("Thanks for playing!")

#---end of the game---#

#Notes: This is a basic demonstration of my ability to create simple interactive games using Python. I had sped through this, and there's a lot room for improvement
