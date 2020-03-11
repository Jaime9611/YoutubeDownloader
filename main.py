from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from ydownloader import download_video


# download function
def download():
    status_dw = download_video(entry.get())
    info.set(status_dw)
    entry.state(['disabled'])

# Clear function
def clear():
    entry.state(['!disabled'])
    entry.delete(0, 'end')
    info.set('Write the link of the video')


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
img_label = ttk.Label(content, image=imgobj, anchor='center')
img_label.grid(column=0, row=0, sticky=(W, E), columnspan=2)

# Label info
info = StringVar()
label_info = ttk.Label(content, textvariable=info, anchor='center')
label_info.grid(column=0, row=1, columnspan=2, sticky=(W, E))
info.set('Write the link of the video')

# entry
link = StringVar()
entry = ttk.Entry(content, textvariable=link)
entry.grid(column=0, row=2, sticky=(W, E), columnspan=2)
root.bind('<Return>', download)


button_dw = ttk.Button(content, 
                   text='Download',
                   command=download)
button_dw.grid(column=0, row=3, sticky=(W, E))

button_cls = ttk.Button(content, 
                   text='Clear',
                   command=clear)
button_cls.grid(column=1, row=3, sticky=W)


root.mainloop() # run the GUI




