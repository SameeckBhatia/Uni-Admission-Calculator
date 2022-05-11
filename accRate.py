#importing libraries and files
from uWaterloo import uw; from uToronto import ut
from ctypes import windll
from tkinter import *
windll.shcore.SetProcessDpiAwareness(1)

#interface initialization
win = Tk()
win.geometry('700x400')

#university options for the dropdown menu
Label(win, text = "Select desired university", font = "Bahnschrift 11").place(x = '50', y = '50')

var1 = StringVar()
var1.set("<university>")
opt1 = ["Toronto", "Waterloo"]

drop1 = OptionMenu(win, var1, *opt1)
drop1.place(x = '50', y = '100')

#university program options for the dropdown menu
Label(win, text = "Select desired program", font = "Bahnschrift 11").place(x = '50', y = '200')

var2 = StringVar()
var2.set("<program>")
opt2 = ["Arts", "Engineering", "Science"]

drop2 = OptionMenu(win, var2, *opt2)
drop2.place(x = '50', y = '250')

#text box to collect input and for user to enter average
Label(win, text = "Enter top 6 average", font = "Bahnschrift 11").place(x = '400', y = '50')
ent1 = Entry(win)
ent1.place(x = '400', y = '100')

#university function
def uni():
    if var1.get() == "Waterloo":
        uw(ent1, var2)
    if var1.get() == "Toronto":
        ut(ent1, var2)

#button to run university function
Button(win, text = "Calculate", command = uni, font = "Bahnschrift 11").place(x = '400', y = '200')

win.mainloop()