#create weather app using pseudocode

import requests
christianapi_code = 'http://api.openweathermap.org/data/2.5/weather?appid=6d77158932922438f202a87183fc0bac&q='
city = input("What city in the United States would you like to check the weather of? ")
requesturl = christianapi_code + city

json_info = requests.get(requesturl).json()
weatherdata = json_info['main']['temp']
#weatherdata = str(weatherdata)

#Kelvin conversion to degrees F
fahrenheit = (weatherdata - 273.15) * 1.8 + 32

print("Looking up the weather for " + city + " now")

fahrenheit = str(fahrenheit) #removing all the unnessary deciamls.
print("The current weather in " + city + " is " + fahrenheit + " degrees fahrenheit")

fahrenheit = int(float(fahrenheit))
if fahrenheit >= 70:
    print("It's a nice day to wear light clothes.")
elif fahrenheit <= 69:
    print('You might want to wear pants and a jacket.')
elif fahrenheit < 5:
    print("It's too cold to go outside.")
elif fahrenheit > 110:
    print("It's too hot to go outside.")


