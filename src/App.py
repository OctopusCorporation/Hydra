# -*- coding: utf-8 -*-
from socketIO_client import SocketIO
import json
import serial

locations=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3']

isOnline = False
for device in locations:  
    try:
        ser = serial.Serial(device, 9600)  
    except:  
        print "Failed to connect on ",device  


def Welcome_response(*args):
    global isOnline
    isOnline = True

def command_Hydra(*args):
    for hydraData in args:
        if isOnline == True:
            decoded = json.loads(hydraData)
            hydraValues = json.loads(json.dumps(decoded['Values'][0]))
            if hydraValues['isOn'] == True:
                ser.write('1')
            else:
                ser.write('0')

socketIO = SocketIO('localhost', 3000)
socketIO.on('Welcome', Welcome_response)
socketIO.on('command.Hydra', command_Hydra)
#socketIO.emit('aaa')
socketIO.wait()