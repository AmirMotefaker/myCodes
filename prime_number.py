# Code by @AmirMotefaker

# # Solution 1 
n=int(input("Enter a number: "))
if n > 1:
    for i in range(2, n//2):
        if(n%i) == 0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is neither prime nor composite")


# # Output:
# # Enter a number: 127
# # 127 is a prime number



# # Solution 2 - CodingYar
user_number = int(input('Enter number: '))

is_prime = True

for i in range (2, user_number):
    if user_number % i == 0:
        is_prime = False
        print(f'{user_number} % {i} ')
        break

if is_prime == True:
    print(f'{user_number} is Prime.')
else:
    print(f'{user_number} is not Prime.')

# Output:
# Enter number: 13
# 13 is Prime.

# Output:
# Enter number: 45
# 45 is not Prime.

# Output:
# Enter number: 1113
# 1113 is not Prime.

# Output:
# Enter number: 1113
# 1113 % 3 
# 1113 is not Prime.

# Output:
# Enter number: 123451
# 123451 % 41         
# 123451 is not Prime.



# Solution Final
import time
start_time = time.time()   #Time at the start of program execution

def is_prime(n):
    avval = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 :
            avval = False
            break
    return avval

prime_count=0
last_prime_number=0

for i in range(1,10001):
    if is_prime(i):
        last_prime_number = i
        prime_count = prime_count + 1

print("")
print ("we had", prime_count, "prime numbers")
print("last prime number was", last_prime_number)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution

# Output:
# we had 1230 prime numbers
# last prime number was 9973
# Time of program execution: 0.06999874114990234
