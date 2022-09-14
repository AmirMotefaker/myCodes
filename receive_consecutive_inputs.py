# Code by AmirMotefaker

# Receive consecutive input from the user

# Solution 1
user_input = int(input('How many numbers? '))

list_of_numbers = []

for i in range(user_input):
    user_number = int(input('Enter your numbers: '))
    list_of_numbers.append(user_number)

print(list_of_numbers)

# Output:
# How many numbers? 3
# Enter your numbers: 1
# Enter your numbers: 2
# Enter your numbers: 3
# [1, 2, 3]



# Solution 2 - While
list_of_numbers = []

while True:
    user_input = input('Enter your number: ')
    if user_input == 'exit':
        break
    list_of_numbers.append(int(user_input))
print(list_of_numbers)


# Output:
# Enter your number: 100
# Enter your number: 12
# Enter your number: 13
# Enter your number: 5
# Enter your number: 0
# Enter your number: 1
# Enter your number: exit
# [100, 12, 13, 5, 0, 1]




# Solution 3 - While with average number input
print('Enter students score. (enter exit to stop)')

list_of_numbers = []

while True:
    user_input = input('Enter your number: ')
    if user_input == 'exit':
        break
    list_of_numbers.append(int(user_input))

print(f'The class average: {sum(list_of_numbers) / len(list_of_numbers)}')
print(f'The Max number is: {max(list_of_numbers)}')
print(f'The Min number is: {min(list_of_numbers)}')

# Output:
# Enter students score. (enter exit to stop)
# Enter your number: 10
# Enter your number: 18
# Enter your number: 19
# Enter your number: 20
# Enter your number: 11
# Enter your number: 12
# Enter your number: 3
# Enter your number: 0
# Enter your number: 17
# Enter your number: exit
# The class average: 12.222222222222221
# The Max number is: 20
# The Min number is: 0
