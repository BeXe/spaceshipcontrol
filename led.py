import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN) #button
GPIO.setup(24,GPIO.OUT) #led
while True:

    # Turn LED off
    print ("LED off")
    GPIO.output(24, GPIO.LOW)
    
    # waiting for button press
    while GPIO.input(23) == 1:
        time.sleep(0.2) 
        
    # Turn LED on
    print ("LED on")
    GPIO.output(24, GPIO.HIGH)


    # waiting for button release
    while GPIO.input(23) == 0:
        time.sleep(0.2)         
		
