from tkinter import *
import os
from functools import partial
from parameters import *
import set
from serialtest import store_values, checkECHO


def AOO():

    modeScreen = Toplevel(set.screen)
    modeScreen.title("AOO")
    modeScreen.geometry("500x1000")
    
    parameters_AOO = ["Mode", "Atrial Pulse Amplitude(V)", "Atrial Pusle Width(ms)", "Lower Rate Limit(ppm)"]

    p0 = 1
    p1 = atrPulseAmp(modeScreen)
    p2 = atrPulseWidth(modeScreen)
    p10 = lowerRateLimit(modeScreen)

    values_AOO = [p0, p1, p2, p10]


    Button(modeScreen, text = "Save and Transmit Values", command = partial(store_values, "AOO", parameters_AOO, values_AOO)).pack(side = "bottom")

def VOO():

    modeScreen = Toplevel(set.screen)
    modeScreen.title("VOO")
    modeScreen.geometry("500x1000")

    parameters_VOO = ["Mode", "Ventricular Pulse Amplitude(V)", "Ventricular Pusle Width(ms)", "Lower Rate Limit(ppm)"]

    p0 = 2
    p5 = venPulseAmp(modeScreen)
    p6 = venPulseWidth(modeScreen)
    p10 = lowerRateLimit(modeScreen)         


    values_VOO = [p0, p5, p6, p10]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "VOO", parameters_VOO, values_VOO)).pack(side = "bottom")
           
def AAI():

    modeScreen = Toplevel(set.screen)
    modeScreen.title("AAI")
    modeScreen.geometry("500x1000")

    parameters_AAI = ["Mode", "Atrial Pulse Amplitude(V)", "Atrial Pusle Width(ms)", "ARP(ms)", "Atrial Sensitivity(V)", "Lower Rate Limit(ppm)"]
    
    p0 = 3
    p1 = atrPulseAmp(modeScreen)
    p2 = atrPulseWidth(modeScreen)
    p3 = ARP(modeScreen)
    p4 = atrSensitivity(modeScreen)
    p10 = lowerRateLimit(modeScreen)    
   
    values_AAI = [p0, p1, p2, p3, p4, p10]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "AAI", parameters_AAI, values_AAI)).pack(side = "bottom")

def VVI():
    modeScreen = Toplevel(set.screen)
    modeScreen.title("VVI")
    modeScreen.geometry("500x1000")
    parameters_VVI = ["Mode", "Ventricular Pulse Amplitude(V)", "Ventricular Pusle Width(ms)", "VRP(ms)", "Ventricular Sensitivity(V)", "Lower Rate Limit(ppm)"]

    p0 = 4
    p5 = venPulseAmp(modeScreen)
    p6 = venPulseWidth(modeScreen)
    p7 = VRP(modeScreen)
    p8 = venSensitivity(modeScreen)
    p10 = lowerRateLimit(modeScreen)       

    values_VVI = [p0, p5, p6, p7, p8, p10]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "VVI", parameters_VVI, values_VVI)).pack(side = "bottom")

def DOO():
    modeScreen = Toplevel(set.screen)
    modeScreen.title("DOO")
    modeScreen.geometry("500x1000")
    parameters_DOO = ["Mode",  "Atrial Pulse Amplitude(V)", "Atrial Pulse Width(ms)", "Ventricular Pulse Amplitude(V)", "Ventricular Pusle Width(ms)", "Fixed AV Delay(ms)","Lower Rate Limit(ppm)"]

    p0 = 5
    p1 = atrPulseAmp(modeScreen)
    p2 = atrPulseWidth(modeScreen)
    p5 = venPulseAmp(modeScreen)
    p6 = venPulseWidth(modeScreen)
    p9 = fixedAVDelay(modeScreen)
    p10 = lowerRateLimit(modeScreen)       

    values_DOO = [p0, p1, p2, p5, p6, p9, p10]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "DOO", parameters_DOO, values_DOO)).pack(side = "bottom")

def AOOR():
    modeScreen = Toplevel(set.screen)
    modeScreen.title("AOOR")
    modeScreen.geometry("500x1000")

    parameters_AOOR = ["Mode", "Atrial Pulse Amplitude(V)", "Atrial Pusle Width(ms)", "Lower Rate Limit(ppm)", "Rate Adaptivity", "Maximum Sensor Rate(ppm)", "Activity Threshold", "Reaction Time(s)",  "Recovery Time(min)", "Response Factor"]

    p0 = 1
    p1 = atrPulseAmp(modeScreen)
    p2 = atrPulseWidth(modeScreen)
    p10 = lowerRateLimit(modeScreen)
    p11 = 1
    p12 = maxSensorRate(modeScreen)
    p13 = actThreshold(modeScreen)
    p14 = reacTime(modeScreen)
    p15 = recoveryTime(modeScreen)
    p16  = resFactor(modeScreen)

    values_AOOR = [p0, p1, p2, p10, p11, p12, p13, p14, p15, p16]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "AOOR", parameters_AOOR, values_AOOR)).pack(side = "bottom")

def AAIR():
    modeScreen = Toplevel(set.screen)
    modeScreen.title("AAIR")
    modeScreen.geometry("500x1000")   

    parameters_AAIR = ["Mode", "Atrial Pulse Amplitude(V)", "Atrial Pusle Width(ms)", "ARP(ms)", "Atrial Sensitivity(V)", "Lower Rate Limit(ppm)", "Rate Adaptivity", "Maximum Sensor Rate(ppm)", "Activity Threshold", "Reaction Time(s)",  "Recovery Time(min)", "Response Factor"]

    p0 = 3
    p1 = atrPulseAmp(modeScreen)
    p2 = atrPulseWidth(modeScreen)
    p3 = ARP(modeScreen)
    p4 = atrSensitivity(modeScreen)
    p10 = lowerRateLimit(modeScreen)
    p11 = 1
    p12 = maxSensorRate(modeScreen)
    p13 = actThreshold(modeScreen)
    p14 = reacTime(modeScreen)
    p15 = recoveryTime(modeScreen)
    p16  = resFactor(modeScreen)

    values_AAIR = [p0, p1, p2, p3, p4, p10, p11, p12, p13, p14, p15, p16]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "AAIR", parameters_AAIR, values_AAIR)).pack(side = "bottom")

def VOOR():
    modeScreen = Toplevel(set.screen)
    modeScreen.title("VOOR")
    modeScreen.geometry("500x1000")
  

    parameters_VOOR = ["Mode", "Ventricular Pulse Amplitude(V)", "Ventricular Pusle Width(ms)", "Lower Rate Limit(ppm)", "Rate Adaptivity", "Maximum Sensor Rate(ppm)", "Activity Threshold", "Reaction Time(s)",  "Recovery Time(min)", "Response Factor"]

    p0 = 2
    p5 = venPulseAmp(modeScreen)
    p6 = venPulseWidth(modeScreen)
    p10 = lowerRateLimit(modeScreen)
    p11 = 1
    p12 = maxSensorRate(modeScreen)
    p13 = actThreshold(modeScreen)
    p14 = reacTime(modeScreen)
    p15 = recoveryTime(modeScreen)
    p16  = resFactor(modeScreen)

    values_VOOR = [p0, p5, p6, p10, p11, p12, p13, p14, p15, p16]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "VOOR", parameters_VOOR, values_VOOR)).pack(side = "bottom")

def VVIR():
    modeScreen = Toplevel(set.screen)
    modeScreen.title("VVIR")
    modeScreen.geometry("500x1000")

    parameters_VVIR = ["Mode", "Ventricular Pulse Amplitude(V)", "Ventricular Pusle Width(ms)", "VRP(ms)", "Ventricular Sensitivity(V)", "Lower Rate Limit(ppm)", "Rate Adaptivity", "Maximum Sensor Rate(ppm)", "Activity Threshold", "Reaction Time(s)",  "Recovery Time(min)", "Response Factor"]

    p0 = 3
    p5 = venPulseAmp(modeScreen)
    p6 = venPulseWidth(modeScreen)
    p7 = VRP(modeScreen)
    p8 = venSensitivity(modeScreen)
    p10 = lowerRateLimit(modeScreen)
    p11 = 1
    p12 = maxSensorRate(modeScreen)
    p13 = actThreshold(modeScreen)
    p14 = reacTime(modeScreen)
    p15 = recoveryTime(modeScreen)
    p16  = resFactor(modeScreen)

    values_VVIR = [p0, p5, p6, p7, p8, p10, p11, p12, p13, p14, p15, p16]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "VVIR",parameters_VVIR, values_VVIR)).pack(side = "bottom")

def DOOR():
    modeScreen = Toplevel(set.screen)
    modeScreen.title("DOOR")
    modeScreen.geometry("500x1000")
    parameters_DOOR = ["Mode",  "Atrial Pulse Amplitude(V)", "Atrial Pulse Width(ms)", "Ventricular Pulse Amplitude(V)", "Ventricular Pusle Width(ms)", "Fixed AV Delay(ms)","Lower Rate Limit(ppm)", "Rate Adaptivity", "Maximum Sensor Rate(ppm)", "Activity Threshold", "Reaction Time(s)",  "Recovery Time(min)", "Response Factor"]

    p0 = 5
    p1 = atrPulseAmp(modeScreen)
    p2 = atrPulseWidth(modeScreen)
    p5 = venPulseAmp(modeScreen)
    p6 = venPulseWidth(modeScreen)
    p9 = fixedAVDelay(modeScreen)
    p10 = lowerRateLimit(modeScreen)
    p11 = 1
    p12 = maxSensorRate(modeScreen)
    p13 = actThreshold(modeScreen)
    p14 = reacTime(modeScreen)
    p15 = recoveryTime(modeScreen)
    p16  = resFactor(modeScreen)

    values_DOOR = [p0, p1, p2, p5, p6, p9, p10, p11, p12, p13, p14, p15, p16]

    Button(modeScreen, text='Save and Transmit Values', command = partial(store_values, "DOOR", parameters_DOOR, values_DOOR)).pack(side = "bottom")

    