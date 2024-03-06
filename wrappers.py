import requests


class CityWeather:
    def __init__(self, name, region, current, feels_like, condition):
        self.city = name
        self.region = region
        self.current = current
        self.feels_like = feels_like
        self.condition = condition

    def __str__(self):
        return f"It is currently {self.condition} and {self.current} in {self.city}, {self.region}. It feels like {self.feels_like}"


class CityAstronomy:
    def __init__(self, name, region, sunrise, sunset, moonrise, moonset, moon_phase):
        self.city = name
        self.region = region
        self.sunrise = sunrise
        self.sunset = sunset
        self.moonrise = moonrise
        self.moonset = moonset
        self.moon_phase = moon_phase

    def __str__(self):
        return f"City: {self.city}\nSunrise: {self.sunrise}\nSunset: {self.sunset}"

class WeatherAPI:
    base_url = 'http://api.weatherapi.com/v1'

    def __init__(self, api_key):
        self.api_key = api_key

    # Private method that will set up the request url, make the get request, and return the JSON response body or None if issue
    # The __ before the function name is a naming convention for making a private method
    #  A Private method is only callable from within the class. Instances do not have access
    def __get(self, city_name, api_method):
        request_url = f"{self.base_url}{api_method}?key={self.api_key}&q={city_name}"
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return None

    # Public method that will take in a city name and return a city object
    def get_current_weather(self, city):
        # Make the API request to get the data
        weather_data = self.__get(city, '/current.json')
        if weather_data:
            city_name = weather_data['location']['name']
            region_name = weather_data['location']['region']
            current_temp = weather_data['current']['temp_f']
            feels_like = weather_data['current']['feelslike_f']
            condition = weather_data['current']['condition']['text']
            # Create a CityWeather instance with above info
            city_obj = CityWeather(city_name, region_name, current_temp, feels_like, condition)
            return city_obj
        else:
            print('No data for the city:', city)

    # Public method that will take in a city name and return a city astro object
    def get_astronomy(self, city):
        # Make the API request to get the data
        astro_data = self.__get(city, '/astronomy.json')
        if astro_data:
            city_name = astro_data['location']['name']
            region_name = astro_data['location']['region']
            sunrise = astro_data['astronomy']['astro']['sunrise']
            sunset = astro_data['astronomy']['astro']['sunset']
            moonrise = astro_data['astronomy']['astro']['moonrise']
            moonset = astro_data['astronomy']['astro']['moonset']
            moon_phase = astro_data['astronomy']['astro']['moon_phase']
            # Create an instance of CityAstronomy with the above data
            city_astro = CityAstronomy(city_name, region_name, sunrise, sunset, moonrise, moonset, moon_phase)
            return city_astro
        else:
            print('No data for the city:', city)
