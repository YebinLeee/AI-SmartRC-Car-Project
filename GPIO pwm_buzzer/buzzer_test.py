import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

buzzer = 17 # buzzer의 핀번호 17
howMany = 1000; # 100번으로 설정

GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(buzzer, False)

try:
    while True:
        if howMany>0:
            howMany -= 1;
            GPIO.output(buzzer, True) # ctrl-c 키 입력되기 전까진 1000번동안 buzzer on/off 실행
            time.sleep(0.001)

            GPIO.output(buzzer, False)
            time.sleep(0.001)
            
        else: break

except KeyboardInterrupt:
    pass

GPIO.output(buzzer, False)

GPIO.cleanup()
