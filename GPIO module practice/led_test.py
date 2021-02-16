import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [5,6,7,8]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, False)

try:
    while True:
        for led in leds:
            GPIO.output(led, True)
            time.sleep(0.5)

        for led in leds:
            GPIO.output(led, False)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass

for led in leds:
    GPIO.output(led, False)

GPIO.cleanup()
