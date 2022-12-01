# Code by AmirMotefaker

# Bitcoin online prices


# run with VPN

# Code#1
import requests

response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
print (response.text)


# Code#2
import requests

response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
print ('at this moment, Bitcoin is %i dollars' % float(response.json()['data']['amount']))



# # Code#3
import requests

def inform_amir():
    print("hi there, price is good.")

my_good_price = 18000
response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(response.json()['data']['amount'])

if price < my_good_price:
    inform_amir()
print (response.text)


# # Code 4
from forex_python.bitcoin import BtcConverter
import time

B = BtcConverter()
for i in  range(10):
    last_price = B.get_latest_price('USD')
    print(last_price)
time.sleep(10)

# Output:
# 20044.4317
# 20044.4317
# 20044.4317
# 20044.4317
# 20044.4317
# 20044.4317
# 20044.4317
# 20044.4317
# 20044.4317
# 20044.4317

