import RPi.GPIO as GPIO # RPi.GPIO 모듈을 GPIO 이름으로 불러옴
import time

led_pin=8 # led_pin을 8번 핀으로 초기화

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

try:
	while True:
		GPIO.output(led_pin, True) # 해당 led핀 on 유지 후 0.5초 지언 
		time.sleep(0.5)
		GPIO.output(led_pin, False) # 해당 led핀 off 유지 후 0.5초 지연
		time.sleep(0.05)
except KeyboardInterrupt: # ctrl-c 입력받으면 종료
    pass

GPIO.cleanup() # 핀 초기화
