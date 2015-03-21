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
            print(decoded['Values'][0])
            ser.write('1')

socketIO = SocketIO('localhost', 3000)
socketIO.on('Welcome', Welcome_response)
socketIO.on('command.Hydra', command_Hydra)
#socketIO.emit('aaa')
socketIO.wait()