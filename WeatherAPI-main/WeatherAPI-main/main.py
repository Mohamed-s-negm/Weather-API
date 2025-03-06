import tkinter as tk
from tkinter import *

FONT_NAME = "Courier"

window = Tk()
window.title("Weather App")
window.geometry("700x500")

title = Label(text="Weather App", font=(FONT_NAME, 20, "bold"))
title.grid(row=0, column=0)

canvas = Canvas(width=300, height=300, highlightthickness=0)
canvas.create_text(100, 150, text="Hello, World!", fill="black", font=(FONT_NAME, 16, "bold"))
canvas.grid(row=1, column=0)

start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"))
start_button.grid(row=2, column=5)



window.mainloop()