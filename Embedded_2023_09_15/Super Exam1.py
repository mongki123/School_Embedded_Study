# Super Challenge1.py

import RPi.GPIO as GPIO
import time

def Setup():

    buzzer_pin = 25
    led_pin1 = 23 # BCM_GPIO 23
    led_pin2 = 24 # BCM_GPIO 24

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(led_pin1, GPIO.OUT)
    GPIO.setup(led_pin2, GPIO.OUT)
    GPIO.setup(buzzer_pin, GPIO.OUT)

    GPIO.output(led_pin1, False)
    GPIO.output(led_pin2, False)

    pwm = GPIO.PWM(buzzer_pin, 1.0)
    pwm.start(0.)

    pwm1 = GPIO.PWM(servo_pin, 50)
    pwm1.start(3.0)

    melody = [262, 294, 330, 349, 392, 440, 494, 523]
    keys = ["a", "s", "d", "f", "g", "h", "j", "k"]

    moterA = DCmoter(26,19,13)

def Information():
    print("LED   on: n , off: m\n")
    print("buzzer   a b c d e f g h => a s d f g h j k")
    print("servo   60 ~ 120: q   30 ~ 150: w   0 ~ 180: e")
    
    return input("dc   forward: t   backward: b \n")
    

def LED():
    global n, m
    
    if userInput == "n" :
        GPIO.output(led_pin1, True)
        GPIO.output(led_pin2, True)
    
    elif userInput == "m" :
        GPIO.output(led_pin1, False)
        GPIO.output(led_pin2, False)
        
def Buzzer():
    global a s d f g h j k
    if 
    for note in range(0, len(keys)) : # len() : 리스트 크기
        if userInput == keys[note] : # 8회 반복하며 입력된 값과 비교
            pwm.ChangeFrequency(melody[note]) # 주파수값 변경 매서드
            pwm.ChangeDutyCycle(50.0)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(0.0)
            break
        
def Servo():
    if userInput == "q" :
        pwm1.ChangeDutyCycle(2.5)
    elif userInput == "w" :
        pwm1.ChangeDutyCycle(7.75)
    elif userInput == "e" :
        pwm1.ChangeDutyCycle(12.5)
        time.sleep(1.0)
        pwm1.ChangeDutyCycle(0.0)

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

def Super():
    
    Setup()
    userInput = Information()
    print(userInput)
    
    LED()
    Buzzer()
    Servo()
    DC()
    

try :
    while True :
        Super()
    
    
except KeyboardInterrupt :
    pass

pwm.stop()
GPIO.cleanup()