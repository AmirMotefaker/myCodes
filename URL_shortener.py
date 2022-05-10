# Code by amotef@gmail.com

# URL Shortener

import pyshorteners   # pyshorteners: A simple URL shortening API wrapper Python library.
long_url = input("Enter the URL to shorten: ")
 
#TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
 
print("The Shortened URL is: " + short_url)
