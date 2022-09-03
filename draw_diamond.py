# Code by AmirMotefaker

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

    

# # Solution 3 - Diamond
# def draw_diamond(num):
#     for i in range(num):
#         if i < num / 2:
#             print(i*2 + 1)

# draw_diamond(7) 

# # Output:
# # 1
# # 3
# # 5
# # 7



# # Solution 4 - Diamond
# def draw_diamond(num):
#     for i in range(num):
#         if i < num / 2:
#             print(i*2 + 1)
#         else:
#             print((num-i)*2 - 1)


# draw_diamond(7)

# # Output:
# # 1
# # 3
# # 5
# # 7
# # 5
# # 3
# # 1



# # Solution 5 - Diamond
# def draw_diamond(num):
#     for i in range(num):
#         if i < num / 2:
#             print((i*2 + 1) * '*')
#         else:
#             print(((num-i)*2 - 1) * '*')


# draw_diamond(7)

# # Output:
# # *
# # ***
# # *****
# # *******
# # *****
# # ***
# # *



# # Solution 6 - Diamond
# def print_star_line(number_of_stars, total_stars):
#     number_of_spaces = (total_stars - number_of_stars) // 2
#     print(f"{' ' * number_of_spaces}{'*' * number_of_stars}{' ' * number_of_spaces}")
    

# def draw_diamond(num):
#     print()
#     for i in range(num):
#         if i < num / 2:
#             print_star_line(i*2 + 1, num)
#         else:
#             print_star_line((num-i)*2 - 1, num)


# draw_diamond(7)

# # Output:
# #    *   
# #   ***
# #  *****
# # *******
# #  *****
# #   ***
# #    *



# # Solution 7 - Diamond
# def print_star_line(number_of_stars, total_stars):
#     number_of_spaces = (total_stars - number_of_stars) // 2
#     print(' ' * number_of_spaces, end='')
#     print('*' * number_of_stars, end='')
#     print(' ' * number_of_spaces)


# def draw_diamond(num):
#     print()
#     for i in range(num):
#         if i < num / 2:
#             print_star_line(i*2 + 1, num)
#         else:
#             print_star_line((num-i)*2 - 1, num)


# draw_diamond(7)

# # Output:
# #    *   
# #   ***
# #  *****
# # *******
# #  *****
# #   ***
# #    *



# # Solution 8 - Diamond
# def print_star_line(number_of_stars, total_stars):
#     number_of_spaces = (total_stars - number_of_stars) // 2
#     print(' ' * number_of_spaces, end='')
#     print('*' * number_of_stars, end='')
#     print(' ' * number_of_spaces)


# def draw_diamond(num):
#     print()
#     number_of_stars = None
#     for i in range(num):
#         if i < num / 2:
#             number_of_stars = i*2 + 1
#         else:
#             number_of_stars = (num-i)*2 - 1

#         print_star_line(number_of_stars, num)

# draw_diamond(7)

# # Output:
# #    *   
# #   ***
# #  *****
# # *******
# #  *****
# #   ***
# #    *



# Solution 9 - user input
def print_star_line(number_of_stars, total_stars):
    number_of_spaces = (total_stars - number_of_stars) // 2
    print(' ' * number_of_spaces, end='')
    print('*' * number_of_stars, end='')
    print(' ' * number_of_spaces)


def draw_diamond(num):
    print()
    number_of_stars = None
    for i in range(num):
        if i < num / 2:
            number_of_stars = i*2 + 1
        else:
            number_of_stars = (num-i)*2 - 1

        print_star_line(number_of_stars, num)


number_of_stars = int(input('Enter number: '))
draw_diamond(number_of_stars)


# Enter number: 7

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
