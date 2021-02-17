import RPi.GPIO as GPIO
import time

buzzer_pin=17 #부저 핀 변수

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer_pin, GPIO.OUT)

pwm=GPIO.PWM(buzzer_pin, 1.0)
pwm.start(50.0)

for cnt in range(0,3):
	pwm.ChangeFrequency(262) # PWM 파형의 주파수를 262로 변경(4옥타브의 도 음에 해당)
	time.sleep(0.5)
	pwm.ChangeFrequency(294) # 294로 변경(4옥타브의 레 음에 해당)
	time.sleep(0.5)
	
pwm.ChangeDutyCycle(0.0) #사각 파형의 HIGH 구간을 0%로 변경. 소리 꺼짐

pwm.stop()
GPIO.cleanup()
