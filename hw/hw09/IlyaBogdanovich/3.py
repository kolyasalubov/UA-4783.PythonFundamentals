import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def format_response(city, weather):
        status = weather.detailed_status.capitalize()
        temp = weather.temperature('celsius')['temp']
        wind = weather.wind()['speed']
        humidity = weather.humidity
        
        final_str = f"City: {city}\nConditions: {status}\nTemp: {temp}°C\nWind: {wind} m/s\nHumidity: {humidity}%"
        return final_str

def get_weather():
    city = entry_field.get()
    
    if not city:
        label.config(text="Please enter a city.")
        return

    observation = mgr.weather_at_place(city)
    w = observation.weather

    result_string = format_response(city, w)
    label.config(text=result_string)


root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 10, 'bold'), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Lower Frame (Results Display)
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), justify='left', anchor='nw', padx=10, pady=10)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()