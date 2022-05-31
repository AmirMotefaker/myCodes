# Code by @AmirMotefaker

# Iterate Over Dictionaries Using for Loop

# Solution 1 - Access both key and value using items()
# dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

# for key, value in dt.items():
#     print(key, value)


# Solution 2 - Access both key and value without using items()
# dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

# for key in dt:
#     print(key, dt[key])


# Solution 3 - Return keys or values explicitly
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt.keys():
    print(key)

for value in dt.values():
    print(value)
    
