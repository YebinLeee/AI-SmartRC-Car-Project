import RPi.GPIO as GPIO
import time

buzzer_pin=17 

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer_pin, GPIO.OUT)

pwm=GPIO.PWM(buzzer_pin, 1.0) # 객체 생성 후 PWM 파형의 주파수를 1.0Hz로 설정
pwm.start(50.0) # PWM 구동 시작(인자 50.0)

melody=[262,294,330,349,392,440,494,523] # 4옥타브의 도 음~ 5옥타브의 도 음~

for note in range(0,8):
	pwm.ChangeFrequency(melody[note])
	time.sleep(0.5)
	
pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()
