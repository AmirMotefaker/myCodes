#Code by @AmirMotefaker

# Handling Exceptions - finally - else

# # Solution 1
a = 10
b = int(input('Enter a number: '))

try:
    print( a / b)
except ZeroDivisionError:
    print('EXCEPTION')


# # Output:
# # Enter a number: 0
# # EXCEPTION



# # Solution 2
a = 10
b = int(input('Enter a number: '))

try: # try to run this code
    print( a / b)
except ZeroDivisionError:
    print('EXCEPTION')
except ModuleNotFoundError:
    print('another exception')
except Exception:
    print('some other error')
else: # if there is no error
    print('ELSE')

print('END')

# # OutPut:
# # Enter a number: 0
# # EXCEPTION
# # END

# # Enter a number: 10
# # 1.0
# # ELSE
# # END


# # Solution 3
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

# # Output:
# # nter a number: 10
# # some other error
# # END



# # Solution 4
a = 10
b = int(input('Enter a number: '))

try: # try to run this code
    b = c + 10
except ZeroDivisionError:
    print('EXCEPTION')
except ModuleNotFoundError:
    print('another exception')
else: # if there is no error
    print('ELSE')

print('END')

# # Output:
# # Enter a number: 10
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\error_handling_finally_else.py", line 78, in <module>
# #     b = c + 10
# # NameError: name 'c' is not defined



# # Solution 5 - finally
a = 10
b = int(input('Enter a number: '))

try: 
    b = c + 10
except ZeroDivisionError:
    print('EXCEPTION')
else: 
    print('ELSE')
finally:
    print('FINALLY')

print('END')

# # Output:
# # Enter a number: 10
# # FINALLY
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\error_handling_finally_else.py", line 102, in <module>
# #     b = c + 10
# # NameError: name 'c' is not defined



# Solution 6 - else- finally
a = 10
b = int(input('Enter a number: '))

try: 
    a = 100
    #b = c + 10
except ZeroDivisionError:
    print('EXCEPTION')
else: 
    print('ELSE')
finally:
    print('FINALLY')

print('END')

# Output:
# Enter a number: 10
# ELSE
# FINALLY
# END
