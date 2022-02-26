
from tkinter import *
import webbrowser as w

win = Tk()
win.title("Webpage Creator")
# Set window size
win.minsize(450,50)
win.maxsize(450,50)
win.configure(background="black")

# Called on button press to create webpage
def createWebpage():
    f = open("customWebpage.html", "a")
    bodyText = v1.get()
    # Writes html file with user added body text included
    f.write("<html><body><h1>{}</h1></body></html>".format(bodyText))
    f.close()
    w.open_new("customWebpage.html")

b1 = Button(win, text = "Create webpage", command=createWebpage)

v1 = StringVar()

e1 = Entry(win, textvariable = v1, width=50)

# Places buttons in the window
b1.pack(side=LEFT, padx=10)
e1.pack(side=LEFT, padx=10)
