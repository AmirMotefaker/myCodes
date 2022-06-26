# Code by @AmirMotefaker

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



## Step 2
# Code by @AmirMotefaker

# Guess the word Game

list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']

def get_input():
    while True:
        user_input = input('Enter your guess: ')  
        if user_input.isalpha():
            return user_input
        print('Your input was not correct. Please enter again.')
    
def print_game_intro():
    print('-'*10)
    print('Hi, Welcome to the Guess Game. ')
    print('All words:', list_of_words)
    print('Please start guessing.')
    print('-'*10)


def run_game():
    print_game_intro()
    print('Number of guessing: 5')
    correct_word = list_of_words[3]

    for i in range(5):
        user_input = get_input()

        if user_input == correct_word:
            print('YOU WON!')
            break
        else:
            print('Your guessed Wrong!')
            print(f'Please try again!, number of rounds left: {4-i}')


run_game()


# Output:
# ----------
# Hi, Welcome to the Guess Game. 
# All words: ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']
# Please start guessing.
# ----------
# Number of guessing: 5
# Enter your guess: son
# Your guessed Wrong!
# Please try again!, number of rounds left: 4
# Enter your guess: paper
# Your guessed Wrong!
# Please try again!, number of rounds left: 3
# Enter your guess: moon
# Your guessed Wrong!
# Please try again!, number of rounds left: 2
# Enter your guess: flower
# Your guessed Wrong!
# Please try again!, number of rounds left: 1
# Enter your guess: hello
# YOU WON!
