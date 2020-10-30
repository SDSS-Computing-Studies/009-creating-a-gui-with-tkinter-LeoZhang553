import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("600x50")

label1 = tk.Label(window,text="x")
label2 = tk.Label(window,text="=")

label1.place(x=150,y=15)
label2.place(x=400,y=15)

window.mainloop()