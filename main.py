
import serial
import time
import RPi.GPIO as GPIO
 

def pumpOn():
    relay1 = 2
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay1, GPIO.OUT)

    GPIO.output(relay1, GPIO.LOW)
    
def pumpOff():
    relay1 = 23
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay1, GPIO.OUT)

    GPIO.output(relay1, GPIO.HIGH)

time.sleep(1)
    
while True:
    
    ser = serial.Serial('/dev/ttyACM0', 9600)
    data = ser.readline().decode('latin-1').strip()
    
    moisture = float(data)
    
    print("Moisture level:", moisture)
    
    pumpOn()

    if moisture < 434:
       print("Moisture level is above 60%. No need to water.") 
          
       if moisture > 434:
          print("Moisture level is below 20%. Watering....")
          pumpOff()
      
    
        
    

 

