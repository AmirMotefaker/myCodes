# Code by amotef@gmail.com

# Currency Converter

from forex_python.converter import CurrencyRates
# forex-python: Forex Python is a Free Foreign exchange rates and currency conversion.

c = CurrencyRates()
amount = int(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)

