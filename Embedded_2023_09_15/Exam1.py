# challenge_01.py

import RPi.GPIO as GPIO

led_pin1 = 23 # BCM_GPIO 23
led_pin2 = 24 # BCM_GPIO 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

GPIO.output(led_pin1, False)
GPIO.output(led_pin2, False)

try :
    while True :
        userInput = input("LED on: n , LED off: m\n") # 키보드 키 값을 받을 변수
        
        print(userInput)
        
        if userInput == "n" :
            GPIO.output(led_pin1, True)
            GPIO.output(led_pin2, True)
            
        elif userInput == "m" :
            GPIO.output(led_pin1, False)
            GPIO.output(led_pin2, False)
            
except KeyboardInterrupt :
    pass

GPIO.cleanup()