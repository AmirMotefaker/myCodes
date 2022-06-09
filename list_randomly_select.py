# Code by @AmirMotefaker

# Randomly Select an Element From the List

# Solution 1 - Using random module
import random

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))


# Solution 2 - Using secrets module
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print(secrets.choice(my_list))
