
from tkinter import *
from tkinter import filedialog as fd


def myBrowse():
    x = fd.askdirectory()
    v1.set(x)
    


win = Tk()

win.title("Check files")
win.configure(background="lightgray")
win.geometry("450x130")

b1 = Button(win, text = "Browse...", width=12, command=myBrowse)
b2 = Button(win, text = "Browse...", width=12)
b3 = Button(win, text = "Check for files...", height=2, width=12)
b4 = Button(win, text = "Close Program", height=2, width=12)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(win, textvariable = v1, width=50)
e2 = Entry(win, textvariable = v2, width=50)

b1.grid(row=2, column=0, padx=10, pady=5)
b2.grid(row=3, column=0, padx=10, pady=5)
b3.grid(row=4, column=0, padx=10, pady=5)
b4.grid(row=4, column=4, padx=10, pady=5)
e1.grid(row=2, column=1, padx=10, pady=5, columnspan=4)
e2.grid(row=3, column=1, padx=10, pady=5, columnspan=4)

