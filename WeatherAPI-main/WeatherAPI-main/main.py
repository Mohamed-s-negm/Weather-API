import tkinter as tk
from tkinter import *

FONT_NAME = "Courier"

window = Tk(screenName="Weather App")
window.title("Weather App")
window.geometry("700x500")

title = Label(text="Weather App", font=(FONT_NAME, 20, "bold"))
title.pack()

city_label = Label(text="City", font=(FONT_NAME, 16, "bold"))
city_label.place(x=100, y=70)
city_entry = Entry(width=10)
city_entry.place(x=100, y=100)

state_code_label = Label(text="State Code", font=(FONT_NAME, 16, "bold"))
state_code_label.place(x=250, y=70)
state_code_entry = Entry(width=10)
state_code_entry.place(x=250, y=100)

country_code_label = Label(text="Country Code", font=(FONT_NAME, 16, "bold"))
country_code_label.place(x=400, y=70)
country_code_entry = Entry(width=10)
country_code_entry.place(x=400, y=100)

start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"))
start_button.place(x=550, y=150)



window.mainloop()