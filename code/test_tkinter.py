from tkinter import *
from tkinter import ttk

root = Tk()

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

nb = ttk.Notebook(root)
nb.pack()

root.mainloop()