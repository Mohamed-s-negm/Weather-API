import tkinter as tk
from tkinter import ttk

window = tk.Tk(screenName="Test")
window.title("Test")
window.geometry("300x200")

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

l1.pack(side=tk.LEFT)
l2.pack(side=tk.RIGHT)

window.mainloop()