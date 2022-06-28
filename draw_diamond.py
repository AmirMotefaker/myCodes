# Code by @AmirMotefaker

# Draw Diamond

# # Solution 1
# def draw_diamond(num):
#     for i in range(1, num, 2):
#         print(i)

#     for i in range(0, num, 2):
#         print(num-i)

# draw_diamond(7)

# # Output:
# # 1
# # 3
# # 5
# # 7
# # 5
# # 3
# # 1



# # Solution 2 - Diamond
# def draw_diamond(num):

#     for i in range(num//2+1):
#         print(i*2 + 1)


# draw_diamond(7) 


# # Output:
# # 1
# # 3
# # 5
# # 7

    

# Solution 3 - Diamond
def draw_diamond(num):
    for i in range(num):
        if i < num / 2:
            print(i*2 + 1)

draw_diamond(7) 

# Output:
# 1
# 3
# 5
# 7
