from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from ydownloader import download_video


# tkinter object
root = Tk()

# root configurations
root.title("YouTube Downloader")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# # main content
content = ttk.Frame(root, padding=(3,3,12,12))
content.grid(column=0, row=0, sticky=(N, E, S, W))
content.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# add logo
img = Image.open('./images/ytlogo.png')
image = img.resize((300, 300), Image.ANTIALIAS) ## The (250, 250) is (height, width)
imgobj = ImageTk.PhotoImage(image)
img_label = ttk.Label(content, image=imgobj)
img_label.grid(column=0, row=0, sticky=(W, E), padx=100)


# entry
link = StringVar()
entry = ttk.Entry(content, textvariable=link)
entry.grid(column=0, row=1, sticky=(W, E), columnspan=2, padx=10)
root.bind('<Return>', lambda i: download_video(entry.get()))



root.mainloop() # run the GUI




