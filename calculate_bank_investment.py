# Code by AmirMotefaker

# Calculate Bank Investment

# r = 0.2

# 1000$ 
# 1200$ = 1000 + (r * 1000) = 1.2 * 1000 =  1200
# 1440$ = 1200 * (1 + r) = 1440
def calc_bank_investment(initial_money, num_of_years, rate=0.2):
    result = initial_money
    
    for i in range(num_of_years):
        result *= (1 + rate)

    return result

print(calc_bank_investment(num_of_years=3, initial_money=1000))
print(1440 * 1.2) # test

# Output:
# 1728.0
# 1728.0
