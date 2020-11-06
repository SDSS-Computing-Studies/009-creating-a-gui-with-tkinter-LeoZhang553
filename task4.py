import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Task3")
window.geometry("475x220")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window,text = "pochacco!")
label3 = tk.Label(window,text = "A cuddy little puppy! This is from the same creator who brought you keropi and kero kero", bg="#A3FFFF")

label1.place(x=100, y=30)
label2.place(x=250, y=50)
label3.place(x=0, y=150)

window.mainloop()