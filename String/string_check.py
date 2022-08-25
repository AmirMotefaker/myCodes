# Code by @AmirMotefaker

# Check If a String Is a Number (Float)

# Solution Using float()
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isfloat('s12'))
print(isfloat('1.123'))
