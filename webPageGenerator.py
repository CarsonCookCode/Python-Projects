
import webbrowser as w

f = open("myWebpage.html", "a")
f.write("<html><body><h1>Stay tuned for our amazing summer sale!</h1></body></html>")
f.close()
w.open_new("myWebpage.html")
