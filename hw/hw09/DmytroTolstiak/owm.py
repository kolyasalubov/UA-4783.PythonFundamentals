from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(sity):
    observation = mgr.weather_at_place(sity)
    w = observation.weather
    return w