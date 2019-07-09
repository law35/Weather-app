print "+----------------------------------------------------------------------------+"
print "|                                 Weather App                                |"
print "+----------------------------------------------------------------------------+"
print "|                            Developed by C.Lawshea.                         |"
print "+----------------------------------------------------------------------------+"


import pyowm
from pyowm import *

owm = pyowm.OWM("API Key goes here")

while True:
	try:
		location = str(raw_input(">>"))
	except ValueError:
		print "Please, enter a valid location."
		continue
	else:
		break
	
	
def observ():
	"""Returns observation."""
	observation = owm.weather_at_place(location) #Sets the location for weather query.
	return observation
	

def weather_data():
	"""Returns weatherData."""
	weatherData = observ().get_weather()
	return weatherData
	
	
def show_temperature():
	"""Prints weather data and temperature."""
	temperature = weather_data().get_temperature("fahrenheit")
	print weather_data()
	print temperature
	
	
def wind_speed():
	"""Prints wind speed."""
	windSpeed = weather_data().get_wind()
	print windSpeed


def tomorrows_forecast():
	"""displays weather conditons for the next seven days."""
	nxtweekForecast = owm.daily_forecast(location, limit=7)#Query for seven day forecast.
	weeksforecast = nxtweekForecast.get_forecast()#Creates a forecast list object.
	
	for weather in weeksforecast:
		print weather.get_reference_time("iso"), weather.get_status()
	
show_temperature()
wind_speed()
tomorrows_forecast()	