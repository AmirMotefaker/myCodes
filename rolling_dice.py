# Code by amotef@gmail.com

# Rolling the dice


## Rolling the dice(Basic)

# import random

# roll_dice = random.randint(1, 6)
# print(roll_dice)


## Rolling the dice(intermediate)

# import random
# run = 1
# level = 0
# while(run == 1):
#         print("**ROUND " + str(level) + "**") 
#         print("player 1: ",random.randint(0, 6))
#         print("player 2: ",random.randint(0, 6))
#         run = int(input("enter 1 to go again or 0 to end: "))
#         print("")
#         level += 1


## Rolling the dice(Dice Roller)

import random

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    
    roll_again = input("Roll the Dices Again?")

