# Code by @AmirMotefaker

# Weather Information

# # Solution 1
# import requests

# api_key = "2cf366b47b474b66d3cb60449bd6f658"  # Enter the API key you got from the OpenWeatherMap website
# base_url = "http://api.openweathermap.org/data/2.5/weather?"

# city_name = input("Enter city name : ")
# complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
# response = requests.get(complete_url)
# x = response.json()

# if x["cod"] != "404":
#     y = x["main"]

#     current_temperature = y["temp"]
#     z = x["weather"]

#     weather_description = z[0]["description"]

#     print(" Temperature (in kelvin unit) = " +
#                     str(current_temperature) +
#           "\n description = " +
#                     str(weather_description))

# else:
#     print(" City Not Found ")



# Solution 2
import requests
import json

API_key = "2cf366b47b474b66d3cb60449bd6f658"
city_name = input("Enter city name: ")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

res = requests.get(URL)
json_data = json.loads(res.text)
weather = json_data["weather"][0]["description"]
temperature = json_data["main"]["temp"]
humidity = json_data["main"]["humidity"]
wind_speed = json_data["wind"]["speed"]

print(f"Weather: {weather}")
print(f"Temperature: {temperature}")
print(f"Humidity: {humidity}")
print(f"Wind Speed: {wind_speed}")


# Output:
# Enter city name: qazvin
# Weather: few clouds
# Temperature: 22.84
# Humidity: 27
# Wind Speed: 4.6

