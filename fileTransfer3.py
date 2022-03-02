
import shutil
import os
import time
from tkinter import *
from tkinter import filedialog as fd

# Allows user to browse and select a source folder
def browseSource():
    x = fd.askdirectory()
    v1.set(x)

# Allows user to browse and select a destination folder
def browseDestination():
    y = fd.askdirectory()
    v2.set(y)

# Checks if files in source folder have been modified in the last 24 hours
# If so, transfers file to destination folder
def transferFiles():
    source = "{}/".format(v1.get())
    destination = "{}/".format(v2.get())
    files = os.listdir(source)
    currentTime = time.time()
    for i in files:
        lastModified = os.path.getmtime(source+i)
        if currentTime - 86400 < lastModified:
            shutil.move(source+i, destination)

# Application GUI
win = Tk()

win.title("Daily Transfer")
win.configure(background="lightgray")
win.geometry("450x170")

l1 = Label(win, text = "Source Folder:", bg="lightgray")
l2 = Label(win, text = "Destination Folder:", bg="lightgray")

b1 = Button(win, text = "Browse...", width=12, command=browseSource)
b2 = Button(win, text = "Browse...", width=12, command=browseDestination)
b3 = Button(win, text = "Transfer Files", height=2, width=12, command=transferFiles)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(win, textvariable = v1, width=50)
e2 = Entry(win, textvariable = v2, width=50)

l1.grid(row=1, column=1)
l2.grid(row=3, column=1)
b1.grid(row=2, column=0, padx=10, pady=5)
b2.grid(row=4, column=0, padx=10, pady=5)
b3.grid(row=5, column=4, padx=10, pady=5)
e1.grid(row=2, column=1, padx=10, pady=5, columnspan=4)
e2.grid(row=4, column=1, padx=10, pady=5, columnspan=4)





