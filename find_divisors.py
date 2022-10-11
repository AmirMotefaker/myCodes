# Code by @AmirMotefaker

# Find Divisors

def divisors(num):
    all_div = [1]

    for i in range(2, num+1):
        if num % i == 0:
            all_div.append(i)

    return all_div

print(divisors(16))


# Output:
# [1, 2, 4, 8, 16]
