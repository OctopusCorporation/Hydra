# -*- coding: utf-8 -*-
from socketIO_client import SocketIO
import json

isOnline = False

def Welcome_response(*args):
    for argumento in args:
        isOnline = True

def command_Hydra(*args):
    for hydraData in args:
        if isOnline == True:
        	print(hydraData)
            #decoded = json.loads(hydraData)
            #print(decoded['Command'])

socketIO = SocketIO('localhost', 3000)
socketIO.on('Welcome', Welcome_response)
socketIO.on('command.Hydra', command_Hydra)
#socketIO.emit('aaa')
socketIO.wait()