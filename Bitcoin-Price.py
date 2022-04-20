# import requests
#
# response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
# print (response)

# https://linuxhit.com/how-to-easily-get-bitcoin-price-quotes-in-python/
import requests
response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
data = response.json()
print(data)


# Me
import requests
def inform_amir():
    print('hi there, price is good.')

my_good_price = 18000
response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD',
                        proxies={'https': 'socks5://127.0.0.1:1080'})
price = float(response.json()['data']['amount'])
#print ('at this moment, Bitcoin is %i dollars' % price)

if (price < my_good_price):
    inform_amir()
