# Code by @AmirMotefaker

# Filter

## Filter1
list_of_scores = [10,5,17,9,11,13,8,19,20]

def is_more_than_15(score):
    if (score >= 15):
        return True
    return False

print(list(filter(is_more_than_15, list_of_scores)))

# Output:
# [17, 19, 20]


## Filter2
list_of_scores = [10,5,17,9,11,13,8,19,20]

def is_more_than_15(score):
    return score >= 15

print(list(filter(is_more_than_15, list_of_scores)))

# Output:
# [17, 19, 20]



## Filter3
names = ['ali alavi sdaf', 'ana', 'sara rezaei', 'shabnam' ]

def example(name):
    if len(name.split()) > 1:
        return True
    return False

print(list(filter(example, names)))

# Output:
# ['ali alavi sdaf', 'sara rezaei']

