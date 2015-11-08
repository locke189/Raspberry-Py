'''
Created on Nov 7, 2015
Don't blink...
@author: Juan_Insuasti
'''

import RPi.GPIO as GPIO
import time

#inicializacion del dispositivo
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#Puertos
led = 2
switch = 3

#inicializacion de los pines
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, GPIO.PUD_UP)

x = 0

ON = 1
OFF = 0
led_state = ON


if __name__ == '__main__':
    # Main Loop
    while x == 0:
        
        if GPIO.input(switch) == True:
            time.sleep(1)
        else:
            time.sleep(0.5)
        
        if led_state == ON:
            led_state = OFF
        else:
            led_state = ON
            
        GPIO.output(led, led_state)

    
    pass