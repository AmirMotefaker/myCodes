# Code by AmirMotefaker

# Nested Loops

for i in range(3):
    print('i loop start')
    
    for j in range(4):
        print('j loop start')
        print(i, j)

    print('-'*10)

# Output:
# i loop start
# j loop start
# 0 0
# j loop start
# 0 1
# j loop start
# 0 2
# j loop start
# 0 3
# ----------
# i loop start
# j loop start
# 1 0
# j loop start
# 1 1
# j loop start
# 1 2
# j loop start
# 1 3
# ----------
# i loop start
# j loop start
# 2 0
# j loop start
# 2 1
# j loop start
# 2 2
# j loop start
# 2 3
# ----------
