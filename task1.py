import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("600x50")

label1 = tk.Label(window,text="x",width=40)
label2 = tk.Label(window,text="=",width=40)

label1.grid(row=1,column=1)
label2.grid(row=1,column=2)

window.mainloop()