import eel
import pyowm


owm = pyowm.OWM("077a74b50d02815176f1da00a0051fc6")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    return "В городе " + place + " сейчас " + str(temp) + " градусов!"

eel.init("web")

eel.start("main.html", size = (700, 700))