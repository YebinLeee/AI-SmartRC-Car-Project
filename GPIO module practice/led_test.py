import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [5,6,7,8] # 리스트를 leds를 5-8번 핀으로 초기화

# 각 핀을 GPIO를 출력한 뒤 off
for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, False)

try:
    while True:
        
        # 각 핀을 차례로 키고 시간 지연
        
        for led in leds:
            GPIO.output(led, True)
            time.sleep(0.5)
            
        #각 핀을 차례로 끄고 시간 지연
        
        for led in leds:
            GPIO.output(led, False)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass

for led in leds:
    GPIO.output(led, False)

GPIO.cleanup()
