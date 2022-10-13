# Code by AmirMotefaker

# Handling Exceptions

nums = [100, -10, 30, 46, 11]

print(f'List of numbers: {nums}')

print('Select one of them with it\'s index.')

index = int(input('Enter index: '))

# def some_error():
#     print(2 / 0)

def get_number_of_list_with_index(list_of_items, index):
    #some_error()
    return(list_of_items[index])

try:
    print(get_number_of_list_with_index(nums, index))
except:
    print('Invalid index...')

print('Some other code running...')


# Output:
# List of numbers: [100, -10, 30, 46, 11]
# Select one of them with it's index.
# Enter index: 3
# 46
# Some other code running...


# Output:
# List of numbers: [100, -10, 30, 46, 11]
# Select one of them with it's index.
# Enter index: 5
# Invalid index...
# Some other code running...

