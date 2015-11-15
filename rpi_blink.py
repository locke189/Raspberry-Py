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
led_green = 2
led_red = 14
led_yellow =4 
switch = 3

#inicializacion de los pines
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)

GPIO.setup(switch, GPIO.IN)

x = 0

ON = 1
OFF = 0
led_state = OFF
led_state_green = OFF
led_state_yellow = OFF

state = 0


if __name__ == '__main__':
    # Main Loop
    while x == 0:
        
        if GPIO.input(switch) == True:
            
            
            if led_state == ON:
                led_state = OFF
                state = 0
            else:
                led_state = ON
                state = 1
            
            GPIO.output(led_red, led_state)
            time.sleep(1)
            
        if state == ON:
                led_state_green = not(led_state_green)
                time.sleep(1)
        else:
                led_state_green = not(led_state_green)
                time.sleep(0.5)
            
        GPIO.output(led_green, led_state_green)

    
    pass