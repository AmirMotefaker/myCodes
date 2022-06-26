# Code by @AmirMotefaker

# Guess the word Game

list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']

def get_input():
    print('-'*10)
    while True:
        user_input = input('Enter your guess: ')  
        if user_input.isalpha():
            return user_input
        print('Your input was not correct. Please enter again.')
    
     
print(get_input())

# Output:
# Enter your guess: heloo232
# Your input was not correct. Please enter again.
# Enter your guess: fdfsdf342@
# Your input was not correct. Please enter again.
# Enter your guess: hello
# hello
