import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Task3")
window.geometry("450x220")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window,text = "pochacco!")
label3 = tk.Label(window,text = "A cuddy little puppy! This is from the same creator who brought you keropi and kero kero", bg="#A3FFFF")

label1.grid(row = 1, column = 1)
label2.grid(row = 1, column = 2)
label3.grid(row = 2, column = 1,columnspan=2)

window.mainloop()