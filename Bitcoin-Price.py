# Code#1
import requests

response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
print (response.text)


# Code#2
import requests

response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
print ('at this moment, Bitcoin is %i dollars' % float(response.json()['data']['amount']))



# Code#3
import requests

def inform_amir():
    print("hi there, price is good.")

my_good_price = 18000
response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(response.json()['data']['amount'])

if price < my_good_price:
    inform_amir()
print (response.text)
