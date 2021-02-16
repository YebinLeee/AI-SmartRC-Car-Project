import RPi.GPIO as GPIO # RPi.GPIO 모듈을 GPIO 이름으로 불러옴
import time

led_pin=7

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT) # led_pin 을 GPIO출력으로 설정

GPIO.output(led_pin, True) # led_pin 을 True로 설정. 연결된 LED가 켜짐

try:
	while True: # 켜진 상태 유지
		pass
except KeyboardInterrupt: # ctrl+c 키 받으면 종료
	pass

GPIO.cleanup() # 핀의 상태 초기화