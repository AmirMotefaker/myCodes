# Code by @AmirMotefaker

# Find Max mark and name in List - Tuples Unpacking

def find_max_mark(mark_list):
    max_mark = 0
    max_mark_name = ''

    for name, mark in mark_list:
        if mark >= max_mark:
            max_mark = mark
            max_mark_name = name

    return max_mark, max_mark_name
    
marks = [('ana', 18), ('arvin', 19), ('sara', 20)]

print(find_max_mark(marks))

# Output:
# (20, 'sara')
