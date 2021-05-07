from tkinter import *
from modes import * 
import os


class lowerRateLimit:
    def __init__(self, root):
        self.number = 12
        self.scale = Scale(root, label = "Lower Rate Limit (ppm)", bg = "green", orient = "horizontal", from_ = 30, to = 175, resolution = 1, length = 600, command = self.changeRes)
        self.scale.set(60)
        self.scale.pack(pady = 2, side="top", fill="y")

    
    def changeRes(self, root):
        if self.scale.get() > 50 and self.scale.get() <= 90:
            self.scale.configure(resolution = 1)
        elif self.scale.get() <= 50:
            self.scale.configure(resolution = 5)
        else:
            self.scale.configure(resolution = 5)

    def final(self):
        return self.scale.get()


class maxSensorRate:
    def __init__(self, root):
        self.number = 14
        self.scale = Scale(root, label = "Maximum Sensor Rate (ppm)", bg = "green", orient = "horizontal", from_ = 50, to = 175, resolution = 5, length = 600)
        self.scale.set(120)
        self.scale.pack(pady = 2)


    def final(self):
            return self.scale.get()

class fixedAVDelay:
    def __init__(self, root):
        self.number = 11
        self.scale = Scale(root, label = "Fixed AV Delay (ms)", bg = "green", orient = "horizontal", from_ = 70, to = 300, resolution = 10, length = 600)
        self.scale.set(150)
        self.scale.pack(pady = 2, side="top", fill="y")


    def final(self):
            return self.scale.get()
        
class atrPulseAmp:
    def __init__(self, root):
        self.number = 3            
        self.scale = Scale(root, label = "Atrial Pulse Amplitude (V)", orient = "horizontal", state = "normal", from_ = 0.1, to = 5,length = 600, resolution = 0.1)
        self.scale.set(5)

        
        self.button1 = Button(root, text =" Use this scale",fg = "red", command = self.enableScale)
        self.button2 = Button(root, text = "Atrial Pulse Amplitude Off",fg = "red", command = self.turnoff)

        
        self.button2.pack(pady = 2, side="top", fill="y")
        self.scale.pack(side="top", fill="y")
        self.button1.pack(side="top", fill="y")

    def enableScale(self):
        self.scale.configure(state = "normal")
        self.scale.configure(bg = "green")


    def turnoff(self):
        self.scale.configure(state = "disabled")
        self.scale.configure(bg = "grey")

    def final(self):
        if self.scale.cget("state") == "disabled":
            return (0)
        elif self.scale.cget("state") == "normal":
            return (self.scale.get())
        else:
            return ("error")
        
class venPulseAmp:
    def __init__(self, root):
        self.number = 7            
        self.scale = Scale(root, label = "Ventricular Pulse Amplitude (V)", orient = "horizontal", state = "normal", from_ = 0.1, to = 5,length = 600, resolution = 0.1)
        self.scale.set(5)

        
        self.button1 = Button(root, text =" Use this scale",fg = "red", command = self.enableScale)
        self.button2 = Button(root, text = "Ventricular Pulse Amplitude Off",fg = "red", command = self.turnoff)
    
        self.button2.pack(pady = 2, side="top", fill="y")
        self.scale.pack(side="top", fill="y")
        self.button1.pack(side="top", fill="y")

    def enableScale(self):
        self.scale.configure(state = "normal")
        self.scale.configure(bg = "green")


    def turnoff(self):
        self.scale.configure(state = "disabled")
        self.scale.configure(bg = "grey")

    def final(self):
        if self.scale.cget("state") == "disabled":
            return (0)
        elif self.scale.cget("state") == "normal":
            return (self.scale.get())
        else:
            return ("error")



class atrPulseWidth:
    def __init__(self, root):
        self.number = 4
        self.scale = Scale(root, label = "Atrial Pulse Width (ms)", bg = "green", orient = "horizontal", from_ = 1, to = 30, resolution = 1, length = 600)
        self.scale.set(1)
        self.scale.pack(pady = 2, side="top", fill="y")


    def final(self):
            return self.scale.get()

class venPulseWidth:
    def __init__(self, root):
        self.number = 8
        self.scale = Scale(root, label = "Ventricular Pulse Width (ms)", bg = "green", orient = "horizontal", from_ = 1, to = 30, resolution = 1, length = 600)
        self.scale.set(1)
        self.scale.pack(pady = 2, side="top", fill="y")


    def final(self):
            return self.scale.get()
    
        
class ARP:
    def __init__(self, root):
        self.number = 5
        self.scale = Scale(root, label = "Atrial Refractory Period (ms)", bg = "green", orient = "horizontal", from_ = 150, to = 500, resolution = 10, length = 600)
        self.scale.set(250)
        self.scale.pack(side="top", fill="y")

    def final(self):
        return self.scale.get()
    
class VRP:
    def __init__(self, root):
        self.number = 9
        self.scale = Scale(root, label = "Ventricular Refractory Period (ms)", bg = "green", orient = "horizontal", from_ = 150, to = 500, resolution = 10, length = 600)
        self.scale.set(320)
        self.scale.pack(side="top", fill="y")

    def final(self):
        return self.scale.get()

       
class atrSensitivity:
    def __init__(self, root):
        self.number = 6
        self.scale = Scale(root, label = "Atrial Sensitivity (V)", bg = "green", orient = "horizontal", from_ = 0, to =5, resolution = 0.1, length = 600)
        self.scale.set(0)
        self.scale.pack(pady = 2, side="top", fill="y")


    def final(self):
            return self.scale.get()

class venSensitivity:
    def __init__(self, root):
        self.number = 10
        self.scale = Scale(root, label = "Ventricular Sensitivity (V)", bg = "green", orient = "horizontal", from_ = 0, to =5, resolution = 0.1, length = 600)
        self.scale.set(0)
        self.scale.pack(pady = 2, side="top", fill="y")


    def final(self):
            return self.scale.get()

class actThreshold:
    def __init__(self, root):
        self.number = 15
        self.radioGroup = LabelFrame(root, text = "Activity Threshold")
        self.radioGroup.pack(side="top", fill="y")

        # Radio variable
        self.level = StringVar()
        # Create two radio buttons
        vlow = Radiobutton(self.radioGroup, text = "V-Low", variable = self.level, value = 0.1)
        low = Radiobutton(self.radioGroup, text = "Low", variable = self.level, value = 0.2)
        medlow = Radiobutton(self.radioGroup, text = "Med-Low", variable = self.level, value = 0.3)
        med = Radiobutton(self.radioGroup, text = "Med", variable = self.level, value = 0.4)
        medhigh = Radiobutton(self.radioGroup, text = "Med-High", variable = self.level, value = 0.5)
        high = Radiobutton(self.radioGroup, text = "High", variable = self.level, value = 0.6)
        vhigh = Radiobutton(self.radioGroup, text = "V-High", variable = self.level, value = 0.7)
        vlow.pack(side = LEFT)
        low.pack(side = LEFT)
        medlow.pack(side = LEFT)
        med.pack(side = LEFT)
        medhigh.pack(side = LEFT)
        high.pack(side = LEFT)
        vhigh.pack(side = LEFT)

        self.level.set(value = 0.4)

    def final(self):
        return (float(self.level.get()))

class reacTime:
    def __init__(self, root):
        self.number = 16
        self.scale = Scale(root, label = "Reaction Time (s)", bg = "green", orient = "horizontal", from_ = 10, to = 50, resolution = 10, length = 600)
        self.scale.set(30)
        self.scale.pack(pady = 2, side="top", fill="y")


    def final(self):
        return self.scale.get()

class resFactor:
    def __init__(self, root):
        self.number = 18    
        self.scale = Scale(root, label = "Response Factor", bg = "green", orient = "horizontal", from_ = 1, to = 16, resolution = 1, length = 600)
        self.scale.set(8)
        self.scale.pack(pady = 2, side="top", fill="y")


    def final(self):
            return self.scale.get()

class recoveryTime:
    def __init__(self, root):
        self.number = 17
        self.scale = Scale(root, label = "Recovery Time (min)", bg = "green", orient = "horizontal", from_ = 2, to = 16, resolution = 1, length = 600)
        self.scale.set(5)
        self.scale.pack(pady = 2, side="top", fill="y")


    def final(self):
        return self.scale.get()
