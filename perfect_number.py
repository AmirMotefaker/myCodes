# Code by AmirMotefaker

# Perfect Number

def divisors(num):
    all_div = []

    for i in range(1, num+1):
        if num % i == 0:
            all_div.append(i)

    return all_div

def is_perfect(num): # 6 # 1, 2, 3, 6
    sum_divs = sum(divisors(num)) - num
    print(f'sum of divisors of {num} is {sum_divs}')
    return  num == sum_divs


print(is_perfect(8128))


# Output:
# sum of divisors of 6 is 6
# True

# Output:
# sum of divisors of 496 is 496
# True

# Output:
# sum of divisors of 8128 is 8128
# True

# Output:
# sum of divisors of 100 is 117
# False

# Output:
# sum of divisors of 1000 is 1340
# False
