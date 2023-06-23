#coding: utf-8
#import webiopi
from hsv import hsv
import os
import datetime

#save directory
SAVEDIR = '/home/pi/mll/Re_Mechanical_Life/foodrecog/foods'
#@webiopi.macro
def camera(no):
    #filename
    filename = SAVEDIR + '/camera_' + no + '.jpg'
    #taking a photo
    command = 'fswebcam -r 320x240 -d /dev/video0 ' + filename
    os.system(command)
    #writing to disk cache
    os.system('sync')
#@webiopi.macro
def date():
    now = datetime.datetime.now()
    NOW = str(now)
    return NOW

camera('1')
#value = hsv()
#print(value)


