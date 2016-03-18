#!/usr/bin/python
import DynamicObjectV2
import os.path
import serial
import time
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
Obj = DynamicObjectV2.Class

ser = serial.Serial("/dev/ttyUSB0",57600)
time.sleep(3)

# put your imports here

def init(self):
    # put your self.registerOutput here
    self.registerOutput("NeoPixle", Obj("Send", False))

def run (self):

    # main loop
    while 1:
        # put your logic here
        # you can use: output, getInputs, message
        NeoP = self.getInputs().colourDTC
        HexV = NeoP.Hex
        Hex = "%s" %HexV
##        print Hex[1:]
##        Red = NeoP.R
##        Gre = NeoP.G
##        Blu = NeoP.B
        ser.write('%s' %(Hex[1:]))

        # if you want to limit framerate, put it at the end
        time.sleep(3)


