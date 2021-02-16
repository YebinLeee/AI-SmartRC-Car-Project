#사용자에게 입력 받아 wheel과 led를 조작

import RPi.GPIO as GPIO

# wheel_control & light_control 모듈의 모든 함수 불러옴
from wheel_control import *
from light_control import *

GPIO.setmode(GPIO.BCM)

dcMotors=[21,18,20,12,22,13,23,19] # 핀번호(wheel 위치/방향)로 초기화
# 순서대로(T/F) left-back / left-front /  right-front / right-back

for dcMotor in dcMotors:
    GPIO.setup(dcMotor, False)
    GPIO.output(dcMotor, False)

leds=[5,6,7,8] # leds 리스트 핀번호로 초기화

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, False)

try:
    while True:

        # 사용자로부터 입력받는 문자에 따라 dcMotors or leds 조작
        
        print('f:forward, b:backward, l:left, r:right, s:stop')
        print('W/w: front light on/off, U/u:rear light on/off')
        print('A/a:all light on/off')
        print('q:quit program')

        cmd=input()
        if cmd=='q':
            break
        
        # wheel control
        if cmd=='f':
            go_forward(dcMotors)
        elif cmd=='b':
            go_backward(dcMotors)
        elif cmd=='l':
            turn_left(dcMotors)
        elif cmd=='r':
            turn_right(dcMotors)

        
        if cmd=='s':
            stop_driving(dcMotors)

        # light control
        if cmd=='W':
            front_light_on(leds)
        elif cmd=='w':
            front-light_off(leds)
        elif cmd=='U':
            rear_light_on(leds)
        elif cmd=='u':
            rear_light_off(leds)
        elif cmd=='A':
            all_light_on(leds)
        elif cmd=='a':
            all_light_off(leds)

except KeyboardInterrupt:
    pass

for dcMotor in dcMotors:
    GPIO.output(dcMotor, False)

for led in leds:
    GPIO.output(led, False)

GPIO.cleanup()
