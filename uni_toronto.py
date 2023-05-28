# importing interface and math libraries
from tkinter import *
from math import *


# toronto probability function
def ut(ent1, var2):
    prog = ["Arts", "Commerce (Toronto)", "Engineering", "Science"]
    mu_values = [85, 88, 90, 88]
    sig_values = [6.5, 3, 5.5, 6.5]

    x = float(ent1.get())

    for i in prog:

        if i == var2.get():
            mu = mu_values[prog.index(i)]
            sig = sig_values[prog.index(i)]

    prob = 0.5 * erf((x - mu) / sig) + 0.5

    # interface configuration
    win = Tk()
    win.geometry("600x200")

    if 0 < x < 100:
        message = Label(win, text="You have a " + str(
            round(100 * prob, 1)) + "%" + " chance of getting an offer",
                        font="Bahnschrift 11")
        message.place(x='50', y='75')
    else:
        message = Label(win, text="Please enter an average in bounds",
                        font="Bahnschrift 11")
        message.place(x='50', y='75')
