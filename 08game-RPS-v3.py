# Code by amotef@gmail.com

# Bazi Sang-Kaghaz-Gheychi
# Game Rock(R)-Paper(P)-Scissors(S) ---> RPS
# version 3

from random import randint

# print("Sang...")
# print("Kaghaz...")
# print("Gheychi...")

#SAng -----> sang
player = input("Player, make your move: ").lower()
rand_num = randint(0, 2) # 0 1 2
if rand_num == 0:
    computer = "sang"
elif rand_num == 1:
    computer = "kaghaz"
else:
    computer = "gheychi"

print(f'computer plays "{computer}"')

if player == computer:
    print("Maghadir mosavi hastand.")
elif player == "sang":
    if computer == "gheychi":
        print("Player 1 wins!")
    elif computer == "kaghaz":
        print("Player 2 wins!")
elif player == "kaghaz":
    if computer == "gheychi":
        print("Player 2 wins!")
    elif computer == "sang":
        print("Player 1 wins!")
elif player == "gheychi":
    if computer == "sang":
        print("Player 2 wins!")
    elif computer == "kaghaz":
        print("Player 1 wins!")
else:
    print("Khatei rokh dadeh ast...")
