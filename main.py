import subprocess
import tkinter.font as font
import tkinter
from tkinter import ttk
import pyglet
from PIL import Image, ImageTk
from tkinter import filedialog as fd


def changeVideo():

    global doneLabel
    global selected_qual


    filename = fd.askopenfilename(title='Select mp4 Snap', initialdir='/', filetypes=[("MP4 only", ".mp4")])

    subprocess.call(['ffmpeg', '-y', '-i', filename, '-crf', selected_qual.get(), '-b:a', '45k', '-vf', 'eq=gamma_b=1.85',  'output/output.mp4'])

    doneLabel.config(text="done ! \nu can find it in the output folder")


pyglet.font.add_file('src/font/Doctor Glitch.otf')


window = tkinter.Tk()
window.geometry("330x300")
window.title("BadFr3nchSnap")
window.maxsize(330, 300)
window.minsize(330, 300)
window.iconbitmap("src/img/icon.ico")
titleFont = font.Font(family='Doctor Glitch', size=20)
mainFont = font.Font(family='Courier', size=13)
littleFont = font.Font(family='Courier', size=11)
littleFont2 = font.Font(family='Courier', size=10)


titleLabel = tkinter.Label(window, text="BadFr3nchSnap", fg="white", bg="black")
titleLabel.place(x=30, y=8)
titleLabel['font'] = titleFont

byLabel = tkinter.Label(window, text="by akira", fg="white", bg="black")
byLabel.place(x=118, y=48)
byLabel['font'] = mainFont


dsd = tkinter.Label(window, text="discord:\nakira#9322", fg="white", bg="black", justify="left")
dsd.place(x=33, y=85)
dsd['font'] = littleFont

github = tkinter.Label(window, text="github:\nakira - trinity", fg="white", bg="black", justify="left")
github.place(x=178, y=85)
github['font'] = littleFont

qualLabel = tkinter.Label(window, text="choose video bitrate :", fg="white", bg="black")
qualLabel.place(x=65, y=125)
qualLabel['font'] = littleFont

qualLabel2 = tkinter.Label(window, text="(an higher value means worst quality)", fg="white", bg="black")
qualLabel2.place(x=20, y=145)
qualLabel2['font'] = littleFont2


selected_qual = tkinter.StringVar()
qual_cb = ttk.Combobox(window, textvariable=selected_qual)
qual_cb["values"] = ["30", "40", "45", "50", "75", "100"]
qual_cb.current(0)
qual_cb['state'] = 'readonly'
qual_cb.place(x=90, y=170)


changeButton = tkinter.Button(window, text="modify snap", bg="black", fg="white", command=changeVideo)
changeButton.place(x=105, y=200)
changeButton['font'] = littleFont

doneLabel=tkinter.Label(window, text="", fg="white", bg="black")
doneLabel.place(x=10, y=240)
doneLabel['font'] = littleFont



window.config(background="black")
window.mainloop()
