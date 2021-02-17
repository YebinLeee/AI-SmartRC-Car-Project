import RPi.GPIO as GPIO

led_pin=7

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

pwm=GPIO.PWM(led_pin, 10.0)
pwm.start(50.0) #0.0~100.0

try:
    while True:
        pass

except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
