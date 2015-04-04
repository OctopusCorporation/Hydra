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
            print "Command received: " + decoded['Command']
            if decoded['Command'] == 'command.compileArduino':
                compile_Arduino(decoded['Values'][0])
            else:
                hydraValues = json.loads(json.dumps(decoded['Values'][0]))
                if hydraValues['isOn'] == True:
                    ser.write('1')
                else:
                    ser.write('0')

def compile_Arduino(args):
    arduinoData = json.loads(json.dumps(args))

    # Create the Arduino Sketch template
    script = "./home/pi/OctopusGIT/Quimera/src/ArduinoCreatorFactory.sh -n %s -i %s" % (arduinoData['appName'], arduinoData['arduinoId'])
    print "ArduinoCreatorFactory.sh is being called..."
    subprocess.call(script, shell=True)
    print "ArduinoCreatorFactory.sh execution is finished"
    # Change the template
    # // Do something


socketIO = SocketIO('localhost', 3000)
socketIO.on('Welcome', Welcome_response)
socketIO.on('command.Hydra', command_Hydra)
socketIO.on('command.compileArduino', command_Hydra)
#socketIO.emit('aaa')
socketIO.wait()