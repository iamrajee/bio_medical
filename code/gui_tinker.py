try:
    import Tkinter
    from Tkinter import *
except:
    import tkinter as Tkinter
    from tkinter import *

# tkinter._test()

window = Tk()
window.title("EOG BASED VIRTUAL KEYBOARD")
window.geometry('640x480')

lbl = Label(window, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)#, state='disabled')
txt.grid(column=1, row=0)

def clicked():
    lbl.configure(text="Button was clicked !! and data="+txt.get(),font=("Arial Bold", 10))
btn = Button(window, text="UP", font=("Arial Bold", 50),bg="black", fg="yellow",command=clicked)
btn.grid(column=2, row=0)
# txt.focus()
window.mainloop()