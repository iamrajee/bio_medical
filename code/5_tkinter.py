try:
    import Tkinter
    from Tkinter import *
except:
    import tkinter as Tkinter
    from tkinter import *

import matplotlib.pyplot as plt
import networkx as nx
import keyboard_config_simple_matrix
keys = keyboard_config_simple_matrix.keys
import pyautogui
import numpy as np
key_state = [1,5]
key_matrix = [
                ['1','2','3','4','5','6','7','8','9','0'],
                ['q','w','e','r','t','y','u','i','o','p'],
                ['a','s','d','f','g','h','j','k','l','Backspace'],
                ['z','x','c','v','b','n','m','Save','Space','Enter']
            ]
key_dict = {}
def find_state(k):
    for i in range(4):
        for j in range(10):
            if key_matrix[i][j] == k:
                return(i,j)
def up():
    if key_state[0] != 0:
        key_state[0]-=1
    else:
        key_state[0]=3
def down():
    if key_state[0] != 3:
        key_state[0]+=1
    else:
        key_state[0]=0
def right():
    if key_state[1] != 9:
        key_state[1]+=1
    else:
        key_state[1]=0
def left():
    if key_state[1] != 0:
        key_state[1]-=1
    else:
        key_state[1]=9

class Keyboard(Tkinter.Frame):
    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)

        btnU = Button(self,text="U", font=("Arial Bold", 50),bg="black", fg="yellow",command=lambda q="U": self.arror_clicked(q))
        btnL = Button(self,text="L", font=("Arial Bold", 50),bg="black", fg="yellow",command=lambda q="L": self.arror_clicked(q))
        btnR = Button(self,text="R", font=("Arial Bold", 50),bg="black", fg="yellow",command=lambda q="R": self.arror_clicked(q))
        btnD = Button(self,text="D", font=("Arial Bold", 50),bg="black", fg="yellow",command=lambda q="D": self.arror_clicked(q))   
        btnU.pack(side='top',expand='no')
        btnD.pack(side='bottom',expand='no')
        btnL.pack(side='left',expand='no')
        btnR.pack(side='right',expand='no')

        
        self.lbl = Label(self, text="Start typing",wraplength=1000 ,font=("Arial Bold", 20),bg="white", fg="black", justify=LEFT)
        self.lbl.pack(expand='no',fill='both', padx=5, pady=5)
        self.lbltxt = ""
        self.bottondict = {}
        self.botton_count = 0
        self.prevbotton = None
        self.inputfile = "save.txt"
        # Function For Creating Buttons
        self.create_frames_and_buttons()

    def create_frames_and_buttons(self):

        # take section one by one
        for key_section in keys:
            # create Sperate Frame For Every Section
            store_section = Tkinter.Frame(self)
            store_section.pack(side='left',expand='yes',fill='both',padx=10,pady=10,ipadx=10,ipady=10)
            
            for layer_name, layer_properties, layer_keys in key_section:
                store_layer = Tkinter.LabelFrame(store_section)#, text=layer_name)
                ##store_layer.pack(side='top',expand='yes',fill='both')
                store_layer.pack(layer_properties)
                for key_bunch in layer_keys:
                    store_key_frame = Tkinter.Frame(store_layer)
                    store_key_frame.pack(side='top',expand='yes',fill='both')
                    for k in key_bunch:
                        k=k.capitalize()
                        if len(k)<=3:
                            store_button = Tkinter.Button(store_key_frame, text=k, width=2, height=2)
                        else:
                            store_button = Tkinter.Button(store_key_frame, text=k.center(5,' '), height=2)
                        if " " in k:
                            store_button['state']='disable'
                        #flat, groove, raised, ridge, solid, or sunken
                        store_button['relief']="sunken"
                        store_button['bg']="powderblue"
                        store_button['command']=lambda q=k: self.button_command(q)
                        store_button.pack(side='left',fill='both',expand='yes')
                        self.bottondict.update({k:store_button})
        return

    # Function For Detecting Pressed Keyword.
    def button_command(self, event):
        original_event = event
        # key_state = 
        self.bottondict[event].configure(bg = "red")
        if 'Save' in event:
            f = open(self.inputfile,"a+")
            updatedtext = self.lbltxt
            f.write(updatedtext)
            f.close()
            if self.prevbotton != None:
                self.bottondict[self.prevbotton].configure(bg = "powderblue")
            self.prevbotton = original_event
            return
        if "Backspace" in event:
            updatedtext = self.lbltxt[:-1]
        elif "Space" in event:
            event = " "
            updatedtext = self.lbltxt+event
        elif 'Enter' in event:
            event = "\n"
            updatedtext = self.lbltxt+event
        else:
            updatedtext = self.lbltxt+event
        
        self.lbl.configure(text=updatedtext, font=("Arial Bold", 10))
        self.lbltxt = updatedtext

        # print(event)
        if self.prevbotton != None:
            self.bottondict[self.prevbotton].configure(bg = "powderblue")
        self.prevbotton = original_event
        return
    def arror_clicked(self,direc):
        if direc == 'U':
            up()
        elif direc == 'D':
            down()
        elif direc == 'L':
            left()
        elif direc == 'R':
            right()
               
        original_event = key_dict[tuple(key_state)]
        # print(direc, key_state, original_event)
        print(original_event)

        #self.button_command(k)
        self.bottondict[original_event].configure(bg = "red")
        if self.prevbotton != None:
            self.bottondict[self.prevbotton].configure(bg = "powderblue")
        self.prevbotton = original_event
        return
# Creating Main Window
def main():
    root = Tkinter.Tk(className=" Python Virtual KeyBoard")

    Keyboard(root).pack(expand='yes',fill='both')
    print(1)
    root.mainloop()
    print(2)
    return

# Function Trigger
if __name__=='__main__':
    #print(keys[0][0][2],type(keys[0][0][2][0]),np.shape(keys))
    for i,e1 in enumerate(keys[0][0][2]):
        #print(i,list(e1))
        for j,e2 in enumerate(list(e1)):
            #print(j,e2)
            key_dict.update({(i,j):e2.capitalize()})
    # print(key_dict)
    main()