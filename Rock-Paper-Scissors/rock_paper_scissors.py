

import random

user_score = 0
computer_score = 0

print("Welcome to Rock Paper Scissors!")

while True:
    user = input("\nEnter rock, paper or scissors (or quit): ").lower()

    if user == "quit":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Goodbye!")
        break

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid input! Try again!")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("Its a Tie!")

    elif user == "rock" and computer == "scissors":
        print("You Win!")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You Win!")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("Score - You:", user_score, "| Computer:", computer_score)
