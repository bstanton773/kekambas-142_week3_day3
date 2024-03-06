from wrappers import WeatherAPI


# client = WeatherAPI('1ac9901266fa4ab48f9185441220510')

# city_name = input('Enter a city to get the info: ').title()

# city_weather = client.get_current_weather(city_name)
# print(city_weather)

# city_astronomy = client.get_astronomy(city_name)
# print(city_astronomy)
# print(city_astronomy.moon_phase)

def main():
    print('Welcome to the weather app. It will tell you the weather for a city.')
    key = input('You need an API Key to use this application. Enter it here: ')
    client = WeatherAPI(key)
    while True:
        city = input('Enter a city name: ').title()
        if city.lower() == 'quit':
            break
        city_weather = client.get_current_weather(city)
        print(city_weather)
        astro = input('Would you like the sunrise/sunset info? y/n ')
        if astro.lower() == 'y':
            city_astro = client.get_astronomy(city)
            print(city_astro)


main()