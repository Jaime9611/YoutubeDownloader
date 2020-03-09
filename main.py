from tkinter import *
from tkinter import ttk


# tkinter object
root = Tk()

# root configurations
root.title("Feet to Meters")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# main content
content = ttk.Frame(root, padding=(3,3,12,12))
content.grid(column=0, row=0, sticky=(N, E, S, W))
content['height'] = 400
content['width'] = 700

root.mainloop() # run the GUI




