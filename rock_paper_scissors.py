# Code by amotef@gmail.com

# Game Rock(R)-Paper(P)-Scissors(S) ---> RPS


# # Solution 1
# from random import randint

# # print("Sang...")
# # print("Kaghaz...")
# # print("Gheychi...")

# #SAng -----> sang
# player = input("Player, make your move: ").lower()
# rand_num = randint(0, 2) # 0 1 2
# if rand_num == 0:
#     computer = "sang"
# elif rand_num == 1:
#     computer = "kaghaz"
# else:
#     computer = "gheychi"

# print(f'computer plays "{computer}"')

# if player == computer:
#     print("Maghadir mosavi hastand.")
# elif player == "sang":
#     if computer == "gheychi":
#         print("Player 1 wins!")
#     elif computer == "kaghaz":
#         print("Player 2 wins!")
# elif player == "kaghaz":
#     if computer == "gheychi":
#         print("Player 2 wins!")
#     elif computer == "sang":
#         print("Player 1 wins!")
# elif player == "gheychi":
#     if computer == "sang":
#         print("Player 2 wins!")
#     elif computer == "kaghaz":
#         print("Player 1 wins!")
# else:
#     print("Khatei rokh dadeh ast...")



# Solution 2 - CodingYar

import random

choices = ['r', 'p', 's']

choice_meaning = {
    'r' : 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}

user_choice = input("Select from Rock, Paper, Scissors: (r, p, s) ")

ai_choice = random.choice(choices)

if user_choice in choices:
    print(f'Your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')
    # r > s - p > r - s > p
    if user_choice == ai_choice:
        print('Tie')
    elif (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r') or (user_choice == 's' and ai_choice == 'p'):
        print('You Won!')
    else:
        print('You Lost!')
else:
    print("Invalid Input")

