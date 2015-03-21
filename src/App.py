# -*- coding: utf-8 -*-
from socketIO_client import SocketIO
import json

isOnline = False

def Welcome_response(*args):
    for argumento in args:
        isOnline = True

def command_Hydra(*args):
    for data in args:
        if isOnline == True:
            decoded = json.loads(data)
            text = "Command: " + decoded['Command'] + ", Values: " + decoded['Values']
            print(text)

socketIO = SocketIO('localhost', 3000)
socketIO.on('Welcome', Welcome_response)
socketIO.on('command.Hydra', command_Hydra)
#socketIO.emit('aaa')
socketIO.wait()