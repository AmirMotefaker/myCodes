# Code by @AmirMotefaker

# Create a Long Multiline String

# Solution 1 - Using triple quotes
my_string = '''The only way to
learn to program is
by writing code.'''

print(my_string)
# output:
# The only way to
# learn to program is
# by writing code.



# Solution 2 - Using parentheses and a single/double quotes
my_string = ("The only way to \n"
        	"learn to program is \n"
        	"by writing code.")

print(my_string)
# output:
# The only way to
# learn to program is
# by writing code.



# Solution 3 - Using \
my_string = "The only way to \n" \
        	"learn to program is \n" \
        	"by writing code."

print(my_string)
# output:
# The only way to
# learn to program is
# by writing code.
