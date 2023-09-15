# challenge_03.py

import RPi.GPIO as GPIO
import time

bp = 25
GPIO.setmode(GPIO.BCM)

GPIO.setup(bp, GPIO.OUT)

pwm = GPIO.PWM(bp, 1.0)
pwm.start(0.0)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
keys = ["a", "s", "d", "f", "g", "h", "j", "k"]

try:
    while True:
        userInput = input("notes(c,d,e,f,g,f,g,c) : a, s, d, f, g, h, j, k \n")
        print(userInput)
        
        for note in range(0, len(keys)):
            if userInput == keys[note]:
                pwm.ChangeFrequency(melody[note])
                pwm.ChangeDutyCycle(50.0)
                time.sleep(0.5)
                pwm.ChangeDutyCycle(0.0)
                break

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()