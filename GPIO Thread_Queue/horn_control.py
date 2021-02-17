import RPi.GPIO as GPIO
import time
		
def horn(buzzer):
	for howMany in range(1000):
		GPIO.output(buzzer, True)
		time.sleep(0.001)
		GPIO.output(buzzer, False)
		time.sleep(0.001)