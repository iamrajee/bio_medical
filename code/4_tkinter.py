try:
    import Tkinter
    from Tkinter import *
except:
    import tkinter as Tkinter
    from tkinter import *

import matplotlib.pyplot as plt
import networkx as nx
import keyboard_config_simple
keys = keyboard_config_simple.keys
import pyautogui

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
        self.bottondict[event].configure(bg = "red")
        if 'Save' in event:
            f = open(self.inputfile,"a+")
            updatedtext = self.lbltxt
            f.write(updatedtext)
            f.close()
            return

        if "Backspace" in event:
            updatedtext = self.lbltxt[:-1]
        elif "space" in event:
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
        print(direc)
        return
# Creating Main Window
def main():
    root = Tkinter.Tk(className=" Python Virtual KeyBoard")
    
    # G=nx.Graph()
    # G.add_nodes_from([1,2,3,4,5,6,7,8,9,0],key="A")
    # G.add_weighted_edges_from([(1,2,1),(2,3,2),(3,4,3),(5,8,4),(9,1,5),(2,3,6),(4,6,7),(8,2,8),(7,3,9)])
    # print(G.nodes(data=True))
    # nx.draw(G)
    # plt.show()

    Keyboard(root).pack(expand='yes',fill='both')

    root.mainloop()
    return

# Function Trigger
if __name__=='__main__':
    main()