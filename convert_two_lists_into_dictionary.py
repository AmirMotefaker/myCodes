# Code by @AmirMotefaker

# Convert Two Lists Into a Dictionary

# Solution 1 - Using zip and dict methods
index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = dict(zip(index, languages))
print(dictionary)

# output:
# {1: 'python', 2: 'c', 3: 'c++'}

