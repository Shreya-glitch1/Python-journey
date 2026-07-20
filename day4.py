print("Rock Paper Scissors Game")
import random
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
possible_choices = ["rock", "paper", "scissors"]
if user_choice not in possible_choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")    

computer_choice = random.choice(possible_choices)
print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
    