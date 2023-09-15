# challenge_02.py

import RPi.GPIO as GPIO

led_pin1 = 23
led_pin2 = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

pwm1 = GPIO.PWM(led_pin1, 1000)
pwm1.start(0)
pwm2 = GPIO.PWM(led_pin2, 1000)
pwm2.start(0)

try:
    while True:
        userInput = input("brightness 0% : 0, 50% : 5, 100% : t \n")
        print(userInput)
        
        if userInput == "0":
            pwm1.ChangeDutyCycle(0)
            pwm2.ChangeDutyCycle(0)
            
        elif userInput == "5":
            pwm1.ChangeDutyCycle(50)
            pwm2.ChangeDutyCycle(50)
        elif userInput == "t":
            pwm1.ChangeDutyCycle(100)
            pwm2.ChangeDutyCycle(100)
            
except KeyboardInterrupt:
    pass

GPIO.cleanup()