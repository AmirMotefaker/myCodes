# Code by AmirMotefaker

# Calculate  min, max, sum, len

# Solution 1
def calc_min_max_sum_len(*args):
    print(type(args))
    for i in args:
        print(i)

calc_min_max_sum_len(1,2,32,1,4,5)

# Output:
# <class 'tuple'>
# 1
# 2
# 32
# 1
# 4
# 5



# # Solution 2
def calc_min_max_sum_len(*args):
    return min(args), max(args), sum(args), len(args)

print(calc_min_max_sum_len(1,2,32,1,4,5,-2,12,0,8))

# # Output:
# # (-2, 32, 63, 10)



# # Solution 3
def calc_min_max_sum_len(*args):
    if len(args) == 0:
        print('Error: At least enter one number')
        return

    sum_result = 0
    max_result = args[0]
    min_result = args[0]
    len_result = 0

    for i in args:
        len_result += 1
        sum_result += i

        if i > max_result:
            max_result = i

        if i < min_result:
            max_result = i
    
    return min_result, max_result, sum_result, len_result


print(calc_min_max_sum_len(1,2,3,4,5,6))

# # Output:
# # (1, 6, 21, 6)



# # Solution 4 - Tuple Unpacking
def calc_min_max_sum_len(*args):
    if len(args) == 0:
        print('Error: At least enter one number')
        return

    sum_result = 0
    max_result = args[0]
    min_result = args[0]
    len_result = 0

    for i in args:
        len_result += 1
        sum_result += i

        if i > max_result:
            max_result = i

        if i < min_result:
            max_result = i
    
    return min_result, max_result, sum_result, len_result


a,b,c,d = calc_min_max_sum_len(1,2,3,4,5)

print(a,b,c,d)

# # Output:
# # 1 5 15 5



# # Solution 5 - Keyword arguments
def calc_min_max_sum_len(*args, list_of_nums):
    sum_result = 0
    max_result = args[0]
    min_result = args[0]
    len_result = 0

    for i in args:
        list_of_nums.append(i)
        len_result += 1
        sum_result += i

        if i > max_result:
            max_result = i

        if i < min_result:
            max_result = i
    
    return min_result, max_result, sum_result, len_result

a= list()
print(calc_min_max_sum_len(1,2,3,4,5,10,list_of_nums=a))

print(a)

# # Output:
# # (1, 10, 25, 6)
# # [1, 2, 3, 4, 5, 10]




# Solution 6 - Keyword arguments - list_of_nums.clear()
def calc_min_max_sum_len(*args, list_of_nums):
    list_of_nums.clear()
    sum_result = 0
    max_result = args[0]
    min_result = args[0]
    len_result = 0

    for i in args:
        list_of_nums.append(i)
        len_result += 1
        sum_result += i

        if i > max_result:
            max_result = i

        if i < min_result:
            max_result = i
    
    return min_result, max_result, sum_result, len_result

a= [0,0,0]
print(calc_min_max_sum_len(1,2,3,4,5,10,list_of_nums=a))

print(a)

# Output:
# (1, 10, 25, 6)
# [1, 2, 3, 4, 5, 10]
