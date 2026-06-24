from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

def get_weather():
    status = w.detailed_status
    temp = w.temperature('celsius')['temp']
    humidity = w.humidity
    wind = w.wind()['speed']

    final_info = (
        f"Detailed_status: {status}\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind: {wind} m/s\n"
        f"{f'Rain: {w.rain}' if w.rain else 'No Rain'}"
        f"\nClouds: {w.clouds}"
        )
    return final_info
    
