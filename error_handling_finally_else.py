# Code by @AmirMotefaker

# Handling Exceptions - finally - else

# # Solution 1
# a = 10
# b = int(input('Enter a number: '))

# try:
#     print( a / b)
# except ZeroDivisionError:
#     print('EXCEPTION')


# # Output:
# # Enter a number: 0
# # EXCEPTION



# # Solution 2
# a = 10
# b = int(input('Enter a number: '))

# try: # try to run this code
#     print( a / b)
# except ZeroDivisionError:
#     print('EXCEPTION')
# except ModuleNotFoundError:
#     print('another exception')
# except Exception:
#     print('some other error')
# else: # if there is no error
#     print('ELSE')

# print('END')

# # OutPut:
# # Enter a number: 0
# # EXCEPTION
# # END

# # Enter a number: 10
# # 1.0
# # ELSE
# # END


# Solution 3
a = 10
b = int(input('Enter a number: '))

try: # try to run this code
    b = c + 10
except ZeroDivisionError:
    print('EXCEPTION')
except ModuleNotFoundError:
    print('another exception')
except Exception:
    print('some other error')
else: # if there is no error
    print('ELSE')

print('END')

# Output:
# nter a number: 10
# some other error
# END
