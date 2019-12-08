
import pyowm


owm = pyowm.OWM('73e9da99ca9166fccf5d75311baf6b73')  # You MUST provide a valid API key



# Search for current weather in a city)
location = input("Please enter location: ")

try:
  observation = owm.weather_at_place(location)
  print(observation)
  w = observation.get_weather()
  status = w.get_status()                    
    
  # Weather details
  date_time= w.get_reference_time(timeformat='iso')
  wind = w.get_wind()                  
  humidity = w.get_humidity()          
  temp = w.get_temperature('celsius')  
  # Search current weather observations in the surroundings of

  print("Today is :",date_time)
  print("Max Temp:",temp['temp_max'],"°C")
  print("Min Temp:", temp['temp_min'], "°C")
  print ("Humidity: ", humidity, "%")
  print("Rainfall Status: ", w.get_detailed_status())
except:
  print ("Location not found")




