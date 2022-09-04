# Code by AmirMotefaker

# Error Handling

# Solution 1
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# Output:
# Please enter a number: a
# Oops!  That was no valid number.  Try again...
# Please enter a number: -d
# Oops!  That was no valid number.  Try again...
# Please enter a number: @
# Oops!  That was no valid number.  Try again...
# Please enter a number: 1
