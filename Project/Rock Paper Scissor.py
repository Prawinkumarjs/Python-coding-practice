# rock paper scissors game

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors ?: ").lower()

    if player == computer:
        print("player: ", player)
        print("Computer:  ", computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("player: ", player)
            print("Computer:  ", computer)
            print("You Lose!")
        if computer == "scissors":
            print("player: ", player)
            print("Computer:  ", computer)
            print("You Win!")
    elif player == "paper":
        if computer == "rock":
            print("player: ", player)
            print("Computer:  ", computer)
            print("You Win!")
        if computer == "scissors":
            print("player: ", player)
            print("Computer:  ", computer)
            print("You Lose!")
    elif player == "scissors":
        if computer == "paper":
            print("player: ", player)
            print("Computer:  ", computer)
            print("You win!")
        if computer == "rock":
            print("player: ", player)
            print("Computer:  ", computer)
            print("You Lose!")

    play_again = input("play again ? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye! ")
