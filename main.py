
import serial
import time
import RPi.GPIO as GPIO


def pumpOn():
    relay1 = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay1, GPIO.OUT)
    GPIO.output(relay1, GPIO.LOW)
    
def pumpOff():
    relay1 = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay1, GPIO.OUT)
    GPIO.output(relay1, GPIO.HIGH)

time.sleep(1)
    
while True:
    
    ser = serial.Serial('/dev/ttyACM0', 9600)
    data = ser.readline().decode('latin-1').strip()
    print(data)
    
    if data >=  400:
        pumpOn()
        
    if data < 300:
        pumpOff()
        
    else:
        print("error ")
    

 

