# 서보모터 예제 2

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class DCmotor() :
    def __init__(self, En, Inx, Iny) : # setting을 위한 생성자매서드, 객체 생성과 함께 실행
        self.En = En
        self.Inx = Inx
        self.Iny = Iny
        GPIO.setup(self.En, GPIO.OUT)
        GPIO.setup(self.Inx, GPIO.OUT)
        GPIO.setup(self.Iny, GPIO.OUT)
        self.pwm = GPIO.PWM(self.En, 100)
        self.pwm.start(0)
        
    def moveF(self, x = 0, t = 0) : # 모터 정회전 매서드, x 는 듀티비, t 는 sleep 시간
        GPIO.output(self.Inx, GPIO.LOW)
        GPIO.output(self.Iny, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
        
    def moveB(self, x = 0, t = 0) : # 모터 역회전 매서드
        GPIO.output(self.Inx, GPIO.HIGH)
        GPIO.output(self.Iny, GPIO.LOW)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
        
    def stop(self, t = 0) : # 모터 정지 매서드
        self.pwm.ChangeDutyCycle(0)
        sleep(t)
        
motorA = DCmotor(26, 19, 13) # 객체생성 : 모터A 인스턴스 선언
motorB = DCmotor(0, 6, 5) # 객체생성 : 모터B 인스턴스 선언
        
try :
    while True :
        #motorA.moveF(70, 1)
        motorB.moveF(70, 1)
        
        #motorA.stop(1)
        motorB.stop(1)
        
        #motorA.moveB(100, 1)
        motorB.moveB(100, 1)
        
        #motorA.stop(1)
        motorB.stop(1)
        
except KeyboardInterrupt :
    pass
GPIO.cleanup()
