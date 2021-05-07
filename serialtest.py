from tkinter import *
import serial
import struct
import set

deviceName = '/dev/tty.usbmodem0006210000001' 
baudRate = 115200

def store_values(mode, parameterNames,parameterValues):
    if set.curruser.get() == "guest":
        errscreen = Toplevel(set.screen) #ensuring session is occuring to quit
        errscreen.title("No session has been started!")
        errscreen.geometry("500x200")
        Label(errscreen,text="Error: please log in to save and transmit data!", fg="red").pack()
    else: 
        to_send = [set.SYNC, set.SET] + [0]*17
        document = str(set.curruser.get()+'.txt')
        f =open(document,"w+")
        f.write("User: " + set.curruser.get() + '\n')
        f.write(mode + '\n')
        for i in range(len(parameterNames)):
            if i == 0:
                to_send[2] = parameterValues[i]
                f.write("Mode: "+ str(parameterValues[0]) + '\n')
            elif parameterNames[i] == "Rate Adaptivity":
                to_send[13] = 1
                f.write("Rate Adaptivity: 1 \n")
            else:
                to_send[parameterValues[i].number] = parameterValues[i].final() 
                f.write(parameterNames[i] + ": " + str(parameterValues[i].final()) + '\n')
        f.close()
        print(to_send)
        
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        packet = struct.pack("<BBBdHHddHHdHHBHdHHB", *to_send)
        device.write(packet)
        print(packet)

def checkECHO():
     with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        data = [set.SYNC, set.ECHO, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        packet = struct.pack("<BBBdHHddHHdHHBHdHHB", *data)
        device.write(packet)
        received = device.read(77) # of unit8 bytes
        packet = struct.unpack("<BdHHddHHdHHBHdHHBdd", received)

        print(packet)
        transmitted = "Mode: {0}, ATR_AMP: {1}, ATR_WIDTH:{2}, ARP: {3}, ATR_SENS: {4}, VENT_AMP: {5}, VENT_WIDTH: {6}, VRP: {7}, VENT_SENS: {8}, AV_DELAY: {9}, LRL: {10}, RATE_ADAP: {11}, MSR: {12}, ACT_THRESH: {13}, REACT_TIME: {14}, RECOV_TIME: {15}, R_FACTOR: {16}, ATR_SIG: {17}, VEN_SIG: {18}".format(*packet)
        print(transmitted)   
        echoscreen = Toplevel(set.screen) #ensuring session is occuring to quit
        echoscreen.title("Data Transmission Status")
        echoscreen.geometry("500x800")
        document = str(set.curruser.get()+'.txt')
        mfile = open(document)
        data = mfile.read()
        mfile.close()
        values = Label(echoscreen, text = data)
        values.pack()
        transmitted = transmitted.split(",")
        f =open("lasttransmitted.txt","w+")
        for i in range(len(transmitted)):
            f.write(transmitted[i] + '\n')
            Label(echoscreen,text=transmitted[i], fg="red").pack()

#[SYNC, ECHO, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'''