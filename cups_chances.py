# Code by AmirMotefaker

# Cups Chances By guessing

import random

cups = int(input('How many cups? '))
chances = int(input('How many chances? '))

ai_goal = random.randint(1, cups)
LINE_LENGTH = 15 # const

print('-'*LINE_LENGTH)
word = 's'

for i in range(chances):
    if chances - i == 1:
        word = ''
    print(f'{chances - i} chance{word} left.')
    user_guess = int(input(f'Guess [1-{cups}]: '))

    if user_guess == ai_goal:
        print('You guessed right.')
        break
    else:
        print('Wrong guess.')

    print('-'*LINE_LENGTH)

if user_guess == ai_goal:
    print('-'*LINE_LENGTH)
    print('You won!')
else:
    print(f'The right answer is {ai_goal}')
    print('You lost. Sorry!')


# Output:
# How many cups? 5
# How many chances? 3
# ---------------
# 3 chances left.
# Guess [1-5]: 2 
# Wrong guess.   
# ---------------
# 2 chances left.
# Guess [1-5]: 3
# Wrong guess.
# ---------------
# 1 chance left.
# Guess [1-5]: 4
# Wrong guess.
# ---------------
# The right answer is 1
# You lost. Sorry!
