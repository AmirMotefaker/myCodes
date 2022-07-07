# Code by @AmirMotefaker

# OOP - Bank Account

# # Solution 1
# import os
# os.system('cls')

# class Deposit:
#     def __init__(self, name, amount =0):
#         self.owner = name
#         self.amount = amount

#     def __str__(self):
#         return f'Owner: {self.owner} | amount: {self.amount}'
    
# john_dep = Deposit('john', 1000)
# david_dep = Deposit('david', 200)

# print (john_dep)

# # Output:
# # Owner: john | amount: 1000



# # Solution 2
# import os
# os.system('cls')

# class Deposit:
#     def __init__(self, name, amount =0):
#         self.owner = name
#         self.amount = amount

#     def __str__(self):
#         return f'Owner: {self.owner} | amount: {self.amount}'

#     def __repr__(self):
#         return f'Deposit(name={self.owner}, amount={self.amount})'

    
# john_dep = Deposit('john', 1000)
# david_dep = Deposit('david', 200)

# print(repr(john_dep))

# # Output:
# # Deposit(name=john, amount=1000)



# # Solution 3 - HardCode
# import os
# os.system('cls')

# class Deposit:
#     def __init__(self, name, amount =0):
#         self.owner = name
#         self.amount = amount

#     def __str__(self):
#         return f'Owner: {self.owner} | amount: {self.amount}'

#     def __repr__(self):
#         return f'{self.__class__.__name__}(name={self.owner}, amount={self.amount})'  # HardCode

    
# john_dep = Deposit('john', 1000)
# david_dep = Deposit('david', 200)

# print(repr(john_dep))

# # Output:
# # Deposit(name=john, amount=1000)



# # Solution 4 - __add__(self, other)
# import os
# os.system('cls')

# class Deposit:
#     def __init__(self, name, amount =0):
#         self.owner = name
#         self.amount = amount

#     def __str__(self):
#         return f'Owner: {self.owner} | amount: {self.amount}'

#     def __repr__(self):
#         return f'{self.__class__.__name__}(name={self.owner}, amount={self.amount})'  # HardCode

#     def __add__(self, other):
#         name = f'{self.owner}+{other.owner}'
#         amount = f'{self.amount}+{other.amount}'
#         return Deposit(name, amount)


    
# john_dep = Deposit('john', 1000)
# david_dep = Deposit('david', 200)

# print(john_dep + david_dep)

# # Output:
# # Owner: john+david | amount: 1000+200



# # Solution 5 - __iadd__(self, other)
# import os
# os.system('cls')

# class Deposit:
#     def __init__(self, name, amount =0):
#         self.owner = name
#         self.amount = amount

#     def __str__(self):
#         return f'Owner: {self.owner} | amount: {self.amount}'

#     def __repr__(self):
#         return f'{self.__class__.__name__}(name={self.owner}, amount={self.amount})'  # HardCode

#     def __add__(self, other):
#         name = f'{self.owner}+{other.owner}'
#         amount = f'{self.amount}+{other.amount}'
#         return Deposit(name, amount)

#     def __iadd__(self, other):
#         self.amount += other.amount
#         other.amount = 0
#         return self


    
# john_dep = Deposit('john', 1000)
# david_dep = Deposit('david', 200)

# john_dep += david_dep
# print(john_dep)
# print(david_dep)

# # Output:
# # Owner: john | amount: 1200
# # Owner: david | amount: 0



# Solution 6 - __eq__(self, other) 
import os
os.system('cls')

class Deposit:
    def __init__(self, name, amount =0):
        self.owner = name
        self.amount = amount

    def __str__(self):
        return f'Owner: {self.owner} | amount: {self.amount}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.owner}, amount={self.amount})'  # HardCode

    def __add__(self, other):
        name = f'{self.owner}+{other.owner}'
        amount = f'{self.amount}+{other.amount}'
        return Deposit(name, amount)

    def __iadd__(self, other):
        self.amount += other.amount
        other.amount = 0
        return self

    def __eq__(self, other):
        return self.amount == other.amount

    
john_dep = Deposit('john', 1000)
david_dep = Deposit('david', 200)

john_dep += david_dep
print(john_dep)
print(david_dep)

print(john_dep == Deposit('', 1200))

# Output:
# Owner: john | amount: 1200
# Owner: david | amount: 0  
# True
