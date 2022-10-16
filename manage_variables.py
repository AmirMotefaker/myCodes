# Code by AmirMotefaker

# How to manage variables in Python

## 1
def custom(num_list):
    a = 2
    num_list.append(1000)

grades = [13,11,17,19,15]
print(grades)
custom(grades)
print(grades)

# Output:
# [13, 11, 17, 19, 15]
# [13, 11, 17, 19, 15, 1000]



## 2
def custom_function(a):
    my_string = 'value1'
    a['key'] = my_string

my_dict = {
    'k1': 'v1',
    'k2': 'v2'
}

print(my_dict)
custom_function(my_dict)
print(my_dict)

# Output:
# {'k1': 'v1', 'k2': 'v2'}
# {'k1': 'v1', 'k2': 'v2', 'key': 'value1'}



## 3
def custom(num_list):
    a = 2
    num_list.append(1000)

grades = [13,11,17,19,15]
print(grades)
custom(grades.copy())
print(grades)

# Output:
# [13, 11, 17, 19, 15]
# [13, 11, 17, 19, 15]



## 4
def custom_function(a):
    my_string = 'value1'
    a['key'] = my_string

my_dict = {
    'k1': 'v1',
    'k2': 'v2'
}

print(my_dict)
custom_function(my_dict.copy())
print(my_dict)

# Output:
# {'k1': 'v1', 'k2': 'v2'}
# {'k1': 'v1', 'k2': 'v2'}



## 5
def custom(num_list):
    copy_num_list = num_list.copy()
    a = 2
    copy_num_list.append(1000)

grades = [13,11,17,19,15]
print(grades)
custom(grades)
print(grades)

# Output:
# [13, 11, 17, 19, 15]
# [13, 11, 17, 19, 15]



## 6
def custom_function(a):
    b = a.copy()
    my_string = 'value1'
    b['key'] = my_string
    b['k1'] = b['k1'] + b['k2']
    print('local', b)

my_dict = {
    'k1': 'v1',
    'k2': 'v2'
}

print('global', my_dict)
custom_function(my_dict)
print('global', my_dict)

# Output:
# global {'k1': 'v1', 'k2': 'v2'}
# local {'k1': 'v1v2', 'k2': 'v2', 'key': 'value1'}
# global {'k1': 'v1', 'k2': 'v2'}



## 7
def custom(num_list):
    copy_num_list = num_list.copy()
    a = 2
    copy_num_list.append(1000)
    return copy_num_list

grades = [13,11,17,19,15]
print(grades)
grades = custom(grades)
print(grades)

# Output:
# [13, 11, 17, 19, 15]
# [13, 11, 17, 19, 15, 1000]
