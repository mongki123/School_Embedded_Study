# plus challenge_01.py

import RPi.GPIO as GPIO

led_pin1 = 23
led_pin2 = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

pwm1 = GPIO.PWM(led_pin1, 1000) # pwm1, 2 객체 선언 및 파형 주기 설정 : 1000Hz
pwm1.start(0) # 듀티비 초기화

pwm2 = GPIO.PWM(led_pin2, 1000)
pwm2.start(0)

try :
    a = 0
    
    while True :
        userInput = input("LED +10% : n , LED -10%: m \n")
        
        print(userInput)
        
        if userInput == "n" :
            a+=10
        elif userInput == "m" :
            a-=10
            
        pwm1.ChangeDutyCycle(a)
        pwm2.ChangeDutyCycle(a)
            
except KeyboardInterrupt :
    pass

GPIO.cleanup()