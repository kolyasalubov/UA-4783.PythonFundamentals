import tkinter as tk
from tkinter import font, messagebox

from pyowm import OWM

HEIGHT = 350
WIDTH = 450
API_KEY = '93ffd418c55612e825059ee2095a9408'

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Output frame (Placed before the function execution)
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# UI Label initialized here so the function can find it
label = tk.Label(lower_frame, font=('Courier', 12), justify='left', anchor='nw', pady=10, padx=10)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

def get_weather():
    city = entry_field.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    
    # Search for current weather in the entered city and get details
    observation = mgr.weather_at_place(city)
    w = observation.weather

    status = w.detailed_status
    temp_dict = w.temperature('celsius')
    current_temp = temp_dict['temp']
    humidity = w.humidity
    wind_dict = w.wind()
    wind_speed = wind_dict.get('speed', 0)
        
        # Format the display string
    weather_info = (
        f"City: {city.title()}\n"
        f"Conditions: {status}\n"
        f"Temperature: {current_temp}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} m/s"
    )

    label['text'] = weather_info

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)    

root.mainloop()
