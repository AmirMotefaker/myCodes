# Code by @AmirMotefaker

# Prime Number

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
