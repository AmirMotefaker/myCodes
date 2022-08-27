# Code by AmirMotefaker

# Access to error content

try:
    print(2/0)
except ZeroDivisionError as e:
    print('EXCEPTION', e)

# Output:
# EXCEPTION division by zero


try:
    import x
except Exception as e:
    print('EXCEPTION', e)

# Output:
# EXCEPTION No module named 'x'



try:
    import x
except ModuleNotFoundError as e:
    print('EXCEPTION', e)

# Output:
# EXCEPTION No module named 'x'
