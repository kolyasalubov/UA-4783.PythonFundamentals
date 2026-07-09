import tkinter as tk
from pyowm import OWM


HEIGHT = 450
WIDTH = 450
WIND_DIRECTION = {
    **dict.fromkeys(range(0, 23), "North"),
    **dict.fromkeys(range(23, 68), "North-East"),
    **dict.fromkeys(range(68, 113), "East"),
    **dict.fromkeys(range(113, 158), "South-East"),
    **dict.fromkeys(range(158, 203), "South"),
    **dict.fromkeys(range(203, 248), "South-West"),
    **dict.fromkeys(range(248, 293), "West"),
    **dict.fromkeys(range(293, 338), "North-West"),
    **dict.fromkeys(range(338, 361), "North"),
}

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather():
    city = entry_field.get()

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        temp = w.temperature('celsius')
        wind = w.wind()
        wind_direction = WIND_DIRECTION.get(wind['deg'], "Unknown")
        weather_info = (
            f"City: {city}\n"
            f"Status: {w.detailed_status}\n"
            f"Temperature: {temp['temp']} °C\n"
            f"Max temperature: {temp['temp_max']} °C\n"
            f"Min temperature: {temp['temp_min']} °C\n"
            f"Raining: {'yes' if w.rain else 'no'}\n"
            f"Humidity: {w.humidity}%\n"
            f"Clouds: {w.clouds}%\n"
            f"Wind: {wind['speed']} m/s\n"
            f"Wind direction: {wind_direction}"
        )

        label.config(text=weather_info)

    except Exception:
        label.config(text="City not found or connection error")



root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14), justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()
