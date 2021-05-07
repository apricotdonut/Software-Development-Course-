from tkinter import *
import newuser
import set
import communicate
import os.path
from os import path




def values():
    if set.curruser.get() == "guest":
        errscreen = Toplevel(set.screen) #ensuring session is occuring to quit
        errscreen.title("No session has been started!")
        errscreen.geometry("500x200")
        Label(errscreen,text="Error: No session is taking place to show any values!", fg="red").pack()
        return
    else:
        valscreen = Toplevel(set.screen)
        if path.exists(set.curruser.get()+'.txt'): #checks to make sure the user has indeed stored something before.
            valscreen.title(str(set.curruser.get())+"'s current selection")
            valscreen.geometry("300x300")
            document = str(set.curruser.get()+'.txt')
            mfile = open(document)
            data = mfile.read()
            mfile.close()
            values = Label(valscreen, text = data)
            values.pack()
        else:
            valscreen.title("Error")
            valscreen.geometry("300x300")
            Label(valscreen, text="You must set parameters before running this task!",fg='red').pack()
        
