# challenge_05.py

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class DCmoter():
    def __init__(self, En, Inx, Iny):
        self.En =En
        self.Inx = Inx
        self.Iny = Iny
        GPIO.setup(self.En, GPIO.OUT)
        GPIO.setup(self.Inx, GPIO.OUT)
        GPIO.setup(self.Iny, GPIO.OUT)
        self.pwm = GPIO.PWM(self.En, 100)
        self.pwm.start(0)
        
    def moveF(self, x = 0, t = 0):
        GPIO.output(self.Inx, GPIO.LOW)
        GPIO.output(self.Iny, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
        
    def moveB(self, x = 0, t = 0):
        GPIO.output(self.Inx, GPIO.HIGH)
        GPIO.output(self.Iny, GPIO.LOW)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
        
    def stop(self, t = 0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)

moterA = DCmoter(26,19,13)
moterB = DCmoter(0, 5, 6)

try:
    while True:
        ui = input("A Forward: at, A Backward: ab \nB Forward: bt, A Backward: bb \n")
        print(ui)
        
        if ui == "at":
            moterA.moveF(100, 1)
            moterA.stop(1)
        elif ui == "ab":
            moterA.moveB(100, 1)
            moterA.stop(1)
        elif ui == "bt":
            moterB.moveF(100, 1)
            moterB.stop(1)
        elif ui == "bb":
            moterB.moveB(100, 1)
            moterB.stop(1)
            
except KeyboardInterrupt:
    pass

GPIO.cleanup()