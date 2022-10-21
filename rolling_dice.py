# Code by AmirMotefaker

# Rolling the dice


## Rolling the dice(Basic)

import random

roll_dice = random.randint(1, 6)
print(roll_dice)


## Rolling the dice(intermediate)

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



## Rolling the dice(advanced)

from random import randint

def roll_dice():
    print(f"Number is: {randint(1,6)}")

roll_dice()   

whatever = 12 # Put the number of times you want to simulate here
for number in range(whatever):
    roll_dice()



## Rolling the dice(advanced+)

from random import randint
repeat = True
while repeat:
    print("You rolled",randint(1,6))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()


## Rolling the dice(advanced+2)

import random
while True:
    print('''1.roll the dice    2.To exit ''')
    user = int(input("what you want to do\n"))
    if user==1:
        number = random.randint(1,6)
        print(number)
    else:
        break
