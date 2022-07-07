# Code by @AmirMotefaker

# OOP - Bank Account

import os
os.system('cls')

class Deposit:
    def __init__(self, name, amount =0):
        self.owner = name
        self.amount = amount

    def __str__(self):
        return f'Owner: {self.owner} | amount: {self.amount}'
    
john_dep = Deposit('john', 1000)
david_dep = Deposit('david', 200)

print (john_dep)

# Output:
# Owner: john | amount: 1000
