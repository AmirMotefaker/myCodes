# # Code by @AmirMotefaker

# Guess the word Game

# ## Step 1
# list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']

# def get_input():
#     print('-'*10)
#     while True:
#         user_input = input('Enter your guess: ')  
#         if user_input.isalpha():
#             return user_input
#         print('Your input was not correct. Please enter again.')
    
     
# print(get_input())

# # Output:
# # Enter your guess: heloo232
# # Your input was not correct. Please enter again.
# # Enter your guess: fdfsdf342@
# # Your input was not correct. Please enter again.
# # Enter your guess: hello
# # hello



# ## Step 2
# list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']

# def get_input():
#     while True:
#         user_input = input('Enter your guess: ')  
#         if user_input.isalpha():
#             return user_input
#         print('Your input was not correct. Please enter again.')
    
# def print_game_intro():
#     print('-'*10)
#     print('Hi, Welcome to the Guess Game. ')
#     print('All words:', list_of_words)
#     print('Please start guessing.')
#     print('-'*10)


# def run_game():
#     print_game_intro()
#     print('Number of guessing: 5')
#     correct_word = list_of_words[3]

#     for i in range(5):
#         user_input = get_input()

#         if user_input == correct_word:
#             print('YOU WON!')
#             break
#         else:
#             print('Your guessed Wrong!')
#             print(f'Please try again!, number of rounds left: {4-i}')


# run_game()


# # Output:
# # ----------
# # Hi, Welcome to the Guess Game. 
# # All words: ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']
# # Please start guessing.
# # ----------
# # Number of guessing: 5
# # Enter your guess: son
# # Your guessed Wrong!
# # Please try again!, number of rounds left: 4
# # Enter your guess: paper
# # Your guessed Wrong!
# # Please try again!, number of rounds left: 3
# # Enter your guess: moon
# # Your guessed Wrong!
# # Please try again!, number of rounds left: 2
# # Enter your guess: flower
# # Your guessed Wrong!
# # Please try again!, number of rounds left: 1
# # Enter your guess: hello
# # YOU WON!


# ## Step 3
# list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']

# def get_input():
#     while True:
#         user_input = input('Enter your guess: ')  
#         if user_input.isalpha():
#             return user_input
#         print('Your input was not correct. Please enter again.')
    
# def print_game_intro():
#     print('-'*10)
#     print('Hi, Welcome to the Guess Game. ')
#     print('All words:', list_of_words)
#     print('Please start guessing.')
#     print('-'*10)


# def run_game(number_of_rounds):
#     print_game_intro()
#     print(f'Number of guessing: {number_of_rounds}')
#     correct_word = list_of_words[3]

#     for i in range(number_of_rounds):
#         user_input = get_input()

#         if user_input.lower() == correct_word:
#             print('YOU WON!')
#             return
#         else:
#             print('Your guessed Wrong!')
#             print(f'Please try again!, number of rounds left: {(number_of_rounds-1)-i}')

#     print('You lose!')

# run_game(3)


# # Output:
# ----------
# # Hi, Welcome to the Guess Game.
# # All words: ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']
# # Please start guessing.
# # ----------
# # Number of guessing: 3
# # Enter your guess: a
# # Your guessed Wrong!
# # Please try again!, number of rounds left: 2
# # Enter your guess: b
# # Your guessed Wrong!
# # Please try again!, number of rounds left: 1
# # Enter your guess: c
# # Your guessed Wrong!
# # Please try again!, number of rounds left: 0
# # You lose!



# ## Step 4
# list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']

# def get_input():
#     while True:
#         user_input = input('Enter your guess: ')  
#         if user_input.isalpha():
#             return user_input
#         print('Your input was not correct. Please enter again.')
    
# def print_game_intro():
#     print('-'*10)
#     print('Hi, Welcome to the Guess Game. ')
#     print('All words:', list_of_words)
#     print('Please start guessing.')
#     print('-'*10)


# def run_game(number_of_rounds):
#     print_game_intro()
#     print(f'Number of guessing: {number_of_rounds}')
#     correct_word = list_of_words[3]

#     for i in range(number_of_rounds):
#         user_input = get_input()

#         while user_input.lower() not in list_of_words:
#             print('You should guess a word from the given words list!')
#             print('Please enter a correct word. ')
#             user_input = get_input()
        
#         if user_input.lower() == correct_word:
#             print('YOU WON!')
#             return
#         else:
#             print('Your guessed Wrong!')
#             print(f'Please try again!, number of rounds left: {(number_of_rounds-1)-i}')

#     print('You lose!')

# run_game(3)


# # Output:
# # ----------
# # Hi, Welcome to the Guess Game. 
# # All words: ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']
# # Please start guessing.
# # ----------
# # Number of guessing: 3
# # Enter your guess: son
# # Your guessed Wrong!
# # Please try again!, number of rounds left: 2
# # Enter your guess: dsad
# # You should guess a word from the given words list!
# # Please enter a correct word.
# # Enter your guess: a
# # You should guess a word from the given words list!
# # Please enter a correct word.
# # Enter your guess: sdsada2313
# # Your input was not correct. Please enter again.
# # Enter your guess: dsad
# # You should guess a word from the given words list!
# # Please enter a correct word.
# # Enter your guess: boy
# # You should guess a word from the given words list!
# # Please enter a correct word.
# # Enter your guess: hello
# # YOU WON!



## Step 5 - FINAL
import random

def get_input():
    while True:
        user_input = input('Enter your guess: ')  
        if user_input.isalpha():
            return user_input
        print('Your input was not correct. Please enter again.')
    
def get_input_from_list(words):
    user_input = get_input()

    while user_input.lower() not in words:
        print('You should guess a word from the given words list!')
        print('Please enter a correct word. ')
        user_input = get_input()

    return user_input.lower()


def print_game_intro():
    print('-'*10)
    print('Hi, Welcome to the Guess Game. ')
    print('All words:', list_of_words)
    print('Please start guessing.')
    print('-'*10)


def run_game(number_of_rounds, words):
    print_game_intro()
    print(f'Number of guessing: {number_of_rounds}')
    correct_word = random.choice(words)

    for i in range(number_of_rounds):
        user_input = get_input_from_list(words)
        
        if user_input == correct_word:
            print('YOU WON!')
            return
        else:
            print('Your guessed Wrong!')
            print(f'Please try again!, number of rounds left: {(number_of_rounds-1)-i}')

    print('You lose!')

list_of_words = "night knight boy manchester usa war knife foxglove thriftless absurd".split()
run_game(5, list_of_words)

# Output:
# ----------
# Number of guessing: 5
# Enter your guess: boy
# Your guessed Wrong!
# Please try again!, number of rounds left: 4
# Enter your guess: night
# Your guessed Wrong!
# Please try again!, number of rounds left: 3
# Enter your guess: knight
# Your guessed Wrong!
# Please try again!, number of rounds left: 2
# Enter your guess: manchester
# Your guessed Wrong!
# Please try again!, number of rounds left: 1
# Enter your guess: BAG
# You should guess a word from the given words list!
# Please enter a correct word.
# Enter your guess: absurd
# Your guessed Wrong!
# Please try again!, number of rounds left: 0
# You lose!
