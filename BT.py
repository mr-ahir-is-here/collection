import serial
import eel
import time
import sys
port="COM12"
eel.init('web')
bluetooth=''
snd='Disconnected '
def sendi(a):
    global snd
    snd=a
@eel.expose
def out():
        return snd
@eel.expose
def ex():
    sys.exit()
@eel.expose
def con():
    try:
        bluetoot=serial.Serial(port, 9600)
        sendi('Conneceted')
        bluetoot.flushInput()
        global bluetooth
        bluetooth=bluetoot

    except Exception as e:    
        print(e)
        pass
@eel.expose
def dcon():
    try:
        global bluetooth
        bluetooth.close()
        bluetooth=''
        sendi('Disconnected.')
    except Exception as e:
        print(e)
        pass
@eel.expose
def send(data):
    try:
        bluetooth.write(bytes(str.encode(data)))
    except:
        pass
@eel.expose
def dj():
   try: 
    for i in range(20):
        bluetooth.write(bytes(str.encode('0')))
        time.sleep(0.003)
        bluetooth.write(bytes(str.encode('1')))
        time.sleep(0.003)
        bluetooth.write(bytes(str.encode('2')))
        time.sleep(0.003)
        bluetooth.write(bytes(str.encode('3')))
        time.sleep(0.003)
        bluetooth.write(bytes(str.encode('2')))
        time.sleep(0.003)
        bluetooth.write(bytes(str.encode('3')))
        time.sleep(0.003)
        bluetooth.write(bytes(str.encode('0')))
        time.sleep(0.003)
        bluetooth.write(bytes(str.encode('1')))
   except:
       pass
a=eel.start('index.html', size=(800, 600))
