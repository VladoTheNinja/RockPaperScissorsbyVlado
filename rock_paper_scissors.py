import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

computer_possibilities = [rock, paper, scissors]

playermove = input("Choose [r]ock, [p]aper or [s]cissors: ")

if playermove == "r":
    playermove = rock
elif playermove == "p":
    playermove = paper
elif playermove == "s":
    playermove = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_move = random.choice(computer_possibilities)


print(f"The computer chose {computer_move}.")

if (playermove == rock and computer_move == scissors) or (playermove == scissors and computer_move == paper) or \
        (playermove == paper and computer_move == rock):
    print("You win")
elif playermove == computer_move:
    print("Draw")
else: print("You lose")