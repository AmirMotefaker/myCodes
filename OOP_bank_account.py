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



# # Solution 7 - transfer(self, other, amount) 
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

#     def __eq__(self, other):
#         return self.amount == other.amount

#     def transfer(self, other, amount):
#         if self.amount < amount:
#             print('Not enough money.')
#             return

#         self.amount -= amount
#         other.amount += amount

    
# john_dep = Deposit('john', 1000)
# david_dep = Deposit('david', 200)

# print(john_dep)
# print(david_dep)

# john_dep.transfer(david_dep, 200)
# print(john_dep)
# print(david_dep)

# # Output:
# # Owner: john | amount: 1000
# # Owner: david | amount: 200
# # Owner: john | amount: 800
# # Owner: david | amount: 400



# # Solution 8 - deposit(self, amount)
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

#     def __eq__(self, other):
#         return self.amount == other.amount

#     def transfer(self, other, amount):
#         if self.amount < amount:
#             print('Not enough money.')
#             return

#         self.amount -= amount
#         other.amount += amount

#     def deposit(self, amount):
#         if amount <= 0:
#             print('Deposit amount should be positive.')
#             return

#         self.amount += amount

    
# john_dep = Deposit('john', 1000)
# david_dep = Deposit('david', 200)

# print(john_dep)
# print(david_dep)
# print('-'*25)

# john_dep.transfer(david_dep, 200)
# print(john_dep)
# print(david_dep)
# print('-'*25)


# john_dep.deposit(2000)
# print(john_dep)
# print(david_dep)


# # Output:
# # Owner: john | amount: 1000
# # Owner: david | amount: 200
# # -------------------------
# # Owner: john | amount: 800
# # Owner: david | amount: 400
# # -------------------------
# # Owner: john | amount: 2800
# # Owner: david | amount: 400



# # Solution 9 - withdraw(self, amount)
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

#     def __eq__(self, other):
#         return self.amount == other.amount

#     def transfer(self, other, amount):
#         if self.amount < amount:
#             print('Not enough money.')
#             return

#         self.amount -= amount
#         other.amount += amount

#     def deposit(self, amount):
#         if amount <= 0:
#             print('Deposit amount should be positive.')
#             return

#         self.amount += amount

#     def withdraw(self, amount):
#         if amount <= 0 or self.amount < amount:
#             print('Amount should be positive.')
#             return

#         if self.amount < amount:
#             print('Not enough money.')
#             return

#         self.amount -= amount
        
    
# john_dep = Deposit('john', 1000)
# david_dep = Deposit('david', 200)
# sara_dep = Deposit('sara')
# david_dep.deposit(2000)

# print(john_dep)
# print(david_dep)
# print('-'*25)

# john_dep.transfer(david_dep, 1000)

# print(john_dep)
# print(david_dep)
# print('-'*25)

# david_dep.transfer(sara_dep, 1340)
# print(john_dep)
# print(david_dep)
# print(sara_dep)

# # Output:
# # Owner: john | amount: 1000
# # Owner: david | amount: 2200
# # -------------------------
# # Owner: john | amount: 0
# # Owner: david | amount: 3200
# # -------------------------
# # Owner: john | amount: 0
# # Owner: david | amount: 1860
# # Owner: sara | amount: 1340



# Solution 10 - repr(sara_dep)
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

    def transfer(self, other, amount):
        if self.amount < amount:
            print('Not enough money.')
            return

        self.amount -= amount
        other.amount += amount

    def deposit(self, amount):
        if amount <= 0:
            print('Deposit amount should be positive.')
            return

        self.amount += amount

    def withdraw(self, amount):
        if amount <= 0 or self.amount < amount:
            print('Amount should be positive.')
            return

        if self.amount < amount:
            print('Not enough money.')
            return

        self.amount -= amount
        
    
john_dep = Deposit('john', 1000)
david_dep = Deposit('david', 200)
sara_dep = Deposit('sara')
david_dep.deposit(2000)

print(john_dep)
print(david_dep)
print('-'*25)

john_dep.transfer(david_dep, 1000)

print(john_dep)
print(david_dep)
print('-'*25)

david_dep.transfer(sara_dep, 1340)
print(john_dep)
print(david_dep)
print(sara_dep)
print('-'*25)

print(repr(sara_dep))

# Output:
# Owner: john | amount: 1000
# Owner: david | amount: 2200
# -------------------------
# Owner: john | amount: 0
# Owner: david | amount: 3200
# -------------------------
# Owner: john | amount: 0
# Owner: david | amount: 1860
# Owner: sara | amount: 1340
# -------------------------
# Deposit(name=sara, amount=1340)
