import tkinter as tk
from tkinter import *
import requests
import json

FONT_NAME = "Courier"
API = "98c9329ae008542ccdf45b8822d95097"

def get_weather(city):
    # Get city name first
    
    # Then use it in the URL
    URL_L = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API}"
    
    response_1 = requests.get(URL_L)
    location_data = response_1.json()
    lat = location_data[0]["lat"]
    lon = location_data[0]["lon"]

    URL_W = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric"
    response = requests.get(URL_W)
    weather_data = response.json()
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]
    
    label_temp.config(text=f"Temperature: {temp}°C")
    label_humidity.config(text=f"Humidity: {humidity}%")
    label_description.config(text=f"Description: {description}")
    label_wind_speed.config(text=f"Wind Speed: {wind_speed} m/s")
    

window = Tk(screenName="Weather App")
window.title("Weather App")
window.geometry("700x500")

title = Label(text="Weather App", font=(FONT_NAME, 20, "bold"))
title.pack()

city_label = Label(text="City", font=(FONT_NAME, 16, "bold"))
city_label.place(x=100, y=70)

city_entry = Entry(width=10)
city_entry.place(x=100, y=100)
city = city_entry.get()

label_temp = Label(text="Temperature", font=(FONT_NAME, 16, "bold"))
label_temp.place(x=100, y=150)

label_humidity = Label(text="Humidity", font=(FONT_NAME, 16, "bold"))
label_humidity.place(x=100, y=200)

label_description = Label(text="Description", font=(FONT_NAME, 16, "bold"))
label_description.place(x=100, y=250)

label_wind_speed = Label(text="Wind Speed", font=(FONT_NAME, 16, "bold"))
label_wind_speed.place(x=100, y=300)


start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"), command=get_weather)
start_button.place(x=550, y=150)



window.mainloop()