# Code by @AmirMotefaker

# Find Divisors

def divisors(num):
    all_div = [1]

    for i in range(2, num+1):
        if num % 2 == 0:
            all_div.append(i)

    return all_div

print(divisors(16))


# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
