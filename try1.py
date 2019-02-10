import math
import time
from picamera import PiCamera
import termios
import sys
import contextlib
import os
import numpy
from PIL import Image
#import bluetooth
import serial
import resizeimage


'''class serialWrapper:
    def __init__(self, device):
        self.ser = serial.Serial('COM1', 9600)
    
    def sendData(self, data):
        data += "\r\n"
        self.ser.write(data.encode())
'''

i = 0
camera = PiCamera()

def size():
    w = input("please enter a width: ")
    h = height("please enter a height: ")
    
def Main():
    i = 0
    print('start')
    #ser = serialWrapper('/dev/ttyUSB0')
    while True:
        camera.capture("images/image"+str(i)+".jpg")
        time.sleep(0.2)
        with open("images/image"+str(i)+".jpg", 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [w, h])
                cover.save("images/image"+str(i)+".jpg", image.format)
            
        im = Image.open("images/image"+str(i)+".jpg")
        np_im = numpy.array(im)
        print (np_im.shape)
        
        np_im = np_im - 18
        new_im = Image.fromarray(np_im)
        new_im.save("numpytest.jpg")
        i += 1
        print(i)
        #ser.sendData(data)
        #if (input(event.key.get_pressed(K_ESCAPE)) == True):
                #sys.exit(0)
        
    
Main()