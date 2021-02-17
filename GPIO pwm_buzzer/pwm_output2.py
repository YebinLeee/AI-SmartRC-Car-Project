import RPi.GPIO as GPIO
import time

led_pin=7

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

pwm=GPIO.PWM(led_pin, 1000.0) #주파수를 늘리면 LED 점멸이 부드러워짐(1.0Hz)
pwm.start(0.0) #0.0~100.0

try:
	while True:
		for t_high in range(0,101):
			pwm.ChangeDutyCycle(t_high) # Dutycycle 주기대로(일정한 리듬) 빛이 on/off 
			time.sleep(0.01)
			
except KeyboardInterrupt:
	pass
	
GPIO.cleanup()
