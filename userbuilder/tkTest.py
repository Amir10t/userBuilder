from tkinter import *

win = Tk()
win.minsize(200,150)
win.maxsize(300,250)
win.geometry("250x200")

Label(win,text ="Frist Name",font='20').pack()
first_name = Entry(win)
first_name.pack()

Label(win,text="Last Name",font='20').pack()
last_name = Entry(win)
last_name.pack()

Button(win,text="sing in",command=None).pack()

win.mainloop()