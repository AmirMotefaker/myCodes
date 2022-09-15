# Code by AmirMotefaker

# Scope Resolution

## Solution 1
user_name = "amir motefaker"

def get_upper_case(my_string):
    """ return the upper case of the input """
    
    return my_string.upper()

def get_title_case(my_string):
    """ return the title case of the input """

    my_string += ' hello'
    return my_string.title()

print(get_title_case(user_name))
print(get_upper_case(user_name))


# Output:
# Amir Motefaker Hello
# AMIR MOTEFAKER



## Solution 2
user_name = "aMir motefaker"
a = 1

def custom_function():
    a = 14
    print(a) 

print(a)

def get_upper_case_first_word(my_string):
    """ return the upper case of the input """
    
    def get_the_first_word(my_string):
        return my_string.split()[0]

    my_string = get_the_first_word(my_string)

    return my_string.upper()

print(get_upper_case_first_word(user_name))

# Output:
# 1
# AMIR

