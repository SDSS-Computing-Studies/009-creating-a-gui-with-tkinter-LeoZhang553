import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("600x200")

label1 = tk.Label(window,text="Client Database")
label2 = tk.Label(window,text="Name")
label3 = tk.Label(window,text="Type")
label4 = tk.Label(window,text="Breed")
label5 = tk.Label(window,text="Owner")
label6 = tk.Label(window,text="Birthdate")


dogphoto = PhotoImage(file="dog.png")
label8 = tk.Label(window, image=dogphoto)

button1 = tk.Button(window,text="<Previous")
button2 = tk.Button(window,text="Save Entry")
button3 = tk.Button(window,text="Next>")

button7 = tk.Button(window,text="search by name",width=15)

entry1 = tk.Entry(window,text="", width=15)
entry2 = tk.Entry(window,text="", width=15)
entry3 = tk.Entry(window,text="", width=15)
entry4 = tk.Entry(window,text="", width=15)
entry5 = tk.Entry(window,text="", width=15)
entry6 = tk.Entry(window,text="", width=25)


button1.place(x=10,y=175)
button2.place(x=270,y=175)
button3.place(x=550,y=175)

entry1.place(x=10,y=150)
entry2.place(x=130,y=150)
entry3.place(x=250,y=150)
entry4.place(x=370,y=150)
entry5.place(x=500,y=150)

label2.place(x=30 ,y=130 )
label3.place(x=150 ,y=130 )
label4.place(x=270 ,y= 130)
label5.place(x= 390,y= 130)
label6.place(x=520 ,y= 130)

label8.place(x=30,y=15)

label1.place(x=270,y=50)

button7.place(x=290,y=12)

entry6.place(x=420,y=15)

window.mainloop()