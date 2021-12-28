#программа определения погоды. Для этого необходимо скачать pip install pyowm
import pyowm
owm = pyowm.OWM ('05ef3e4d373438ae1b72806a84649ee1')  # You MUST provide a valid API key
place=input("В каком городе/стране?: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
print("В городе" + place + "сейчас " + w.get_detailed_status())