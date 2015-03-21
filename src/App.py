# -*- coding: utf-8 -*-
from socketIO_client import SocketIO
import json
import serial

isOnline = False
ser = serial.Serial('/dev/ttyACM0', 9600)

def Welcome_response(*args):
    global isOnline
    isOnline = True

def command_Hydra(*args):

    for hydraData in args:
        if isOnline == True:
            decoded = json.loads(hydraData)
            hydraValues = json.loads(decoded['Values'][0])
            if hydraValues['isOn'] == True:
                ser.write('1')
            else:
                ser.write('0')

socketIO = SocketIO('localhost', 3000)
socketIO.on('Welcome', Welcome_response)
socketIO.on('command.Hydra', command_Hydra)
#socketIO.emit('aaa')
socketIO.wait()