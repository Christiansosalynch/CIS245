
def main():

    import urllib
    from urllib.request import urlopen
    def internet():
        try:
            urlopen('https://www.google.com', timeout=1)
            return True
        except urllib.error.URLError as Error:
            print(Error)
            return False
    if internet():
        pass
    else:
        print('Connection failed. Please check you are connected to the internet and then try the program again.')
        exit()

    import requests


    christianapi_code = 'http://api.openweathermap.org/data/2.5/weather?appid=6d77158932922438f202a87183fc0bac&q='
    city = input("What city in the United States would you like to check the weather of? ")
    requesturl = christianapi_code + city
    try:
        urlopen(requesturl, timeout=1)
    except urllib.error.URLError as Error:
        print(Error)
        print('The city requested does not exist, please check spelling and run the program again.')
        return False
    json_info = requests.get(requesturl).json()
    weatherdata = json_info['main']['temp']
    # weatherdata = str(weatherdata)

    # Kelvin conversion to degrees F
    fahrenheit = (weatherdata - 273.15) * 1.8 + 32
    print("Looking up the weather for " + city + " now")

    fahrenheit = str(fahrenheit)  # removing all the unnessary deciamls.
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

    restart = input("Would you like to look up another city? Type 'yes' or 'no'. ").lower()
    if restart == "yes":
        main()

    else:
        exit()


main()
