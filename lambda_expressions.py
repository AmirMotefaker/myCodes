# Code by @AmirMotefaker

# Lambda Expressions

## example
list_of_scores = [2,10,5,17,9,11,13,8,19,20]

def is_more_than_15(score): return score >= 15

print(list(filter(is_more_than_15, list_of_scores)))

# Output:
# [17, 19, 20]



## Lambda1
list_of_scores = [2,10,5,17,9,11,13,8,19,20]

# def is_more_than_15(score): return score >= 15
lambda score: score >= 15

print(list(filter(is_more_than_15, list_of_scores)))

# Output:
# [17, 19, 20]



## Lambda2
list_of_scores = [2,10,5,17,9,11,13,8,19,20]

# def x(score):
#     return score >= 15

x = lambda score: score >= 15

print(list(filter(x, list_of_scores)))

# Output:
# [17, 19, 20]



## Lambda3
list_of_scores = [2,10,5,17,9,11,13,8,19,20]

# def x(score):
#     return score >= 15

print(list(filter(lambda score: score >= 15, list_of_scores)))

# Output:
# [17, 19, 20]



## Lambda4
names = ['ali alavi', 'ana johnson', 'baran barani']

def extract_name(full_name):
    return full_name.split()[0]

# lambda full_name: full_name.split()[0]

print(list(map(extract_name, names)))

# Output:
# ['ali', 'ana', 'baran']



## Lambda5
names = ['ali alavi', 'ana johnson', 'baran barani']

print(list(map(lambda full_name: full_name.split()[0], names)))

# Output:
# ['ali', 'ana', 'baran']


## Lambda6
numbers = [5,6,20,1,34,6]

print(list(map(lambda num: num+1, numbers)))

# Output:
# [6, 7, 21, 2, 35, 7]



## Lambda7
numbers = [5,6,20,1,34,6]

for i in map(lambda num: num+1, numbers):
    print(i)

# Output:
# 6
# 7
# 21
# 2
# 35
# 7



## Lambda8  
numbers = [5,6,20,1,34,6]  # ['AAAAA', 'AAAAAA',  ]

for i in map(lambda num: 'A'*num, numbers):
    print(i)

# Output:
# AAAAA
# AAAAAA
# AAAAAAAAAAAAAAAAAAAA
# A
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAA



## Lambda9 
numbers = [5,6,20,1,34,6]  # ['AAAAA', 'AAAAAA',  ]

for i in map(lambda x: 'A'*x, numbers):
    print(i)

# Output:
# AAAAA
# AAAAAA
# AAAAAAAAAAAAAAAAAAAA
# A
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAA
