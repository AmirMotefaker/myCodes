# Code by amotef@gmail.com

# Rolling the dice


# Rolling the dice(Basic)

# import random

# roll_dice = random.randint(1, 6)
# print(roll_dice)


# Rolling the dice(intermediate)

import random
run = 1
level = 0
while(run == 1):
        print("**ROUND " + str(level) + "**") 
        print("player 1: ",random.randint(0, 6))
        print("player 2: ",random.randint(0, 6))
        run = int(input("enter 1 to go again or 0 to end: "))
        print("")
        level += 1

