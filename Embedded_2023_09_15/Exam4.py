# challenge_04.py

import RPi.GPIO as GPIO
import time

sp = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(sp, GPIO.OUT)

pwm = GPIO.PWM(sp, 50)
pwm.start(3.0)

try:
    while True:
        ui = input("angle 0: q, angle 90: w, angle: 180: e \n")
        print(ui)
        
        if ui == "q":
            pwm.ChangeDutyCycle(2.5)
        elif ui == "w":
            pwm.ChangeDutyCycle(7.75)
        elif ui == "e":
            pwm.ChangeDutyCycle(12.5)
            
        time.sleep(1.0)
        pwm.ChangeDutyCycle(0.0)
        
except KeyboardInterrupt:
    pass

pwm.ChangeDutyCycle(3.0)
time.sleep(1.0)
pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()