# import modules
try:
    import Tkinter
except:
    import tkinter as Tkinter

import keyboard_config_simple
keys = keyboard_config_simple.keys
import pyautogui

##  Frame Class
class Keyboard(Tkinter.Frame):
    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)

        # Function For Creating Buttons
        self.create_frames_and_buttons()

    # Function For Extracting Data From KeyBoard Table
    # and then provide us a well looking
    # keyboard gui
    def create_frames_and_buttons(self):
        # take section one by one
        for key_section in keys:
            # create Sperate Frame For Every Section
            store_section = Tkinter.Frame(self)
            store_section.pack(side='left',expand='yes',fill='both',padx=10,pady=10,ipadx=10,ipady=10)
            
            for layer_name, layer_properties, layer_keys in key_section:
                store_layer = Tkinter.LabelFrame(store_section)#, text=layer_name)
                #store_layer.pack(side='top',expand='yes',fill='both')
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
        return

    # Function For Detecting Pressed Keyword.
    def button_command(self, event):
        print(event)
        return

# Creating Main Window
def main():
    root = Tkinter.Tk(className=" Python Virtual KeyBoard")
    Keyboard(root).pack()
    root.mainloop()
    return

# Function Trigger
if __name__=='__main__':
    main()