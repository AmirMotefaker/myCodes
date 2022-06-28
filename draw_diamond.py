# Code by @AmirMotefaker

# Draw Diamond

def draw_diamond(num):
    for i in range(1, num, 2):
        print(i)

    for i in range(0, num, 2):
        print(num-i)

draw_diamond(7)

# Output:
# 1
# 3
# 5
# 7
# 5
# 3
# 1
