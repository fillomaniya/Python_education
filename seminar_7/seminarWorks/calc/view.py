import model
from tkinter import *
from tkinter import ttk

root = None
frm = None

def createMenu():
    global root
    global frm
    root = Tk()
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Button( frm, text = "Дни до Нового года", command=printResult).grid(column=0, row=1)
    ttk.Button( frm, text = "Quit", command=root.destroy).grid(column=1, row=5)
    root.mainloop()

def printResult():
    global frm
    ttk.Label(frm, text=f'{model.newYear()} дней до Нового Года').grid(column=1, row=1)

