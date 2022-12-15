# Code by mirMotefaker

# Changing Global Variables

a = 2
 
def custom_function(num):
    global a
    a = a + num
    print(a)

print(a)
custom_function(100)
print(a)

# Output:
# 2
# 102
# 102
