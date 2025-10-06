import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import requests
import json
#import ttkbootstrap as ttkb
# Weather App using Tkinter and OpenWeatherMap API

def func_get_weather():
    city = select_city.get()
    if city:
        messagebox.showinfo("Weather Info", f"Fetching weather for {city}...")
        api_key="f5c96844ab85ac21566fb8b4e751f1f0"
        api_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        data=requests.get(api_url).json()
        #Filtering the data
        temp=data["main"]["temp"]
        humidity=data["main"]["humidity"]
        wind=data["wind"]["speed"]
        #pressure=data["main"]["pressure"]
       # description=data["weather"][0]["description"]
        #messagebox.showinfo("Weather Info", f"Temperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind} m/s\nPressure: {pressure} hPa\nDescription: {description}")
        output_label.config(text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind} m/s ")
        output_label.pack(pady=10)
    else:
        messagebox.showwarning("Input Error", "Please select a city.")











root = tk.Tk()
root.geometry("400x450")
root.title("Weather App")
root.configure(bg="#FEF8DD")
root.resizable(False, False)



app_header=tk.Label(root, text="Weather Application", font=("Georgia", 20), bg="white", fg="black")
app_header.pack(pady=10)


city_label = tk.Label(root, text="Select City Name:", font=("Arial", 14), bg="#FEF8DD")
city_label.pack(pady=50)

select_city=ttk.Combobox(root, width=30, font=("Arial", 12))
select_city['values'] = ("Amritsar", "Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore", "Hyderabad", "Pune", "Jaipur", "Lucknow")
select_city.pack(pady=10)


select_button=tk.Button(root, text="GET WEATHER", font=("Arial", 12),command=func_get_weather)
select_button.pack(pady=10)

output_label = tk.Label(root, text=" ", font=("Arial", 12), bg="#FEF8DD")







root.mainloop()