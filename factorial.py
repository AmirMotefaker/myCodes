# Code by AmirMotefaker

# Factorial

# 3! = 1 * 2 * 3 = 6
# 5! = 1 * 2 * 3 * 4 * 5 = 125

def factorial(n):
    result = 1

    for i in range(2, n+1):
            result *= i

    return result

print(factorial(5))

# Output:
# 120
