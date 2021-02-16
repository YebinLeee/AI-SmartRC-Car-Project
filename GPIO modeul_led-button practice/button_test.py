import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

buttons = [16]

for button in buttons:
    GPIO.setup(button, GPIO.IN)

try:
    while True:
        for button in buttons:
            print(GPIO.input(button))
            
except KeyboardInterrupt:
    pass

GPIO.cleanup()
