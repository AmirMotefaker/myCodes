# Code by AmirMotefaker

# Return Multiple Values From a Function

# Solution 1 - Return values using comma
def name():
    return "Amir","Motefaker"

# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2 = name()
print(name_1, name_2)


# Output:
# ('Amir', 'Motefaker')
# Amir Motefaker



# Solution 2 -  Using a dictionary
def name():
    n1 = "Amir"
    n2 = "Motefaker"

    return {1:n1, 2:n2}

names = name()
print(names)


# Output:
# {1: 'Amir', 2: 'Motefaker'}
