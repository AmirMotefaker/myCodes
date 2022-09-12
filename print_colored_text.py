# Code by AmirMotefaker

# Print Colored Text to the Terminal

# Solution 1 - Using ANSI escape sequences
print('\x1b[38;2;5;86;243m' + 'Programiz' + '\x1b[0m')



# Solution 2 - Using python module termcolor
from termcolor import colored

print(colored('Programiz', 'blue'))
