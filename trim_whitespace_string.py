# Code by @AmirMotefaker

# Trim Whitespace From a String

# Solution 1 - Using strip()
# my_string = " Python "

# print(my_string.strip())

# Output:
# Python

# my_string = " \nPython "

# print(my_string.strip(" "))


# Output:
# Python


# Solution 2 - Using regular expression
import re

my_string  = " Hello Python "
output = re.sub(r'^\s+|\s+$', '', my_string)

print(output)

# Output:
# Hello Python
