#importing interface and math libraries
from tkinter import *
from math import *

#waterloo probability function
def uo(ent1, var2):
    prog = ["Arts", "Engineering", "Science"]
    mu_values = [85, 89, 89]
    sig_values = [4, 4, 5.5]

    x = float(ent1.get())

    for i in prog:

        if i == var2.get():
            mu = mu_values[prog.index(i)]
            sig = sig_values[prog.index(i)]

    prob = 0.5*erf((x-mu)/sig)+0.5
    
    #interface configuration
    win = Tk()
    win.geometry("600x200")
    
    if x > 0 and x < 100:
        message = Label(win, text = "You have a " + str(round(100*prob, 1)) + "%" + " chance of getting an offer", font = "Bahnschrift 11")
        message.place(x = '50', y = '75')
    else:
        message = Label(win, text = "Please enter an average in bounds", font = "Bahnschrift 11")
        message.place(x = '50', y = '75')