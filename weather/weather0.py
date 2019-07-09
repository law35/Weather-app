import pyowm

owm = pyowm.OWM("API Key goes here")
location = str(raw_input(">>"))

observation = owm.weather_at_place(location) #Sets the location for weather query. 

weatherData = observation.get_weather() #Instance of get_weather() function.

windSpeed = weatherData.get_wind()

temperature = weatherData.get_temperature("fahrenheit")

tomorrowForecast = pyowm.timeutils.tomorrow()

print weatherData
print windSpeed
print temperature
print tomorrowForecast