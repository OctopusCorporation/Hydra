# -*- coding: utf-8 -*-
from socketIO_client import SocketIO
import json
import serial
import subprocess

locations=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3']

isOnline = False
# Detect and select the Serial Port
for device in locations:  
    try:
        ser = serial.Serial(device, 9600)
        break
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

def compile_Arduino(*args):
    for hydraData in args:
        dataDecoded = json.loads(hydraData)
        hydraValues = json.loads(json.dumps(decoded['Values'][0]))
        script = "./home/pi/OctopusGIT/Quimera/src/ArduinoCreatorFactory.sh -n %s -i %s" % (hydraValues['appName'], hydraValues['arduinoId'])
        print "ArduinoCreatorFactory.sh is being called..."
        subprocess.call(script, shell=True)
        print "ArduinoCreatorFactory.sh execution is finished"


socketIO = SocketIO('localhost', 3000)
socketIO.on('Welcome', Welcome_response)
socketIO.on('command.Hydra', command_Hydra)
socketIO.on('command.compileArduino', command_Hydra)
#socketIO.emit('aaa')
socketIO.wait()