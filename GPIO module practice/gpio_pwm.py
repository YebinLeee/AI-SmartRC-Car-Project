# LED 점멸 반복하기

import RPi.GPIO as GPIO # Rpi.GPIO.PWM 모듈을 불러 GPIO로 부른다

led_pin=8 # 사용할 6번 핀 변수 초기화

GPIO.setmode(GPIO.BCM) # BCM GPIO 핀 번호 사용하도록 설정

GPIO.setup(led_pin, GPIO.OUT) #led_pin을 GPIO 출력으로 설정

#GPIO.PWM 객체 생성하고 1.0Hz의 주파수 생성, 파형 구간 설정
pwm = GPIO.PWM(led_pin, 1.0)
pwm.start(50.0)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.setup()
