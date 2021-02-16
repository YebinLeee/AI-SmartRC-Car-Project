# RPi.GPIO 모듈을 이용하여 leds 리스트에 저장돼 있는 led(핀번호 5~8)를 조작하는 함수들을 정의한 패키지이다.


import RPi.GPIO as GPIO
import time

def front_left_on(leds) :
	GPIO.output(leds[1], True)

def front_left_off(leds) :
	GPIO.output(leds[1], False)

def front_right_on(leds) :
	GPIO.output(leds[0], True)

def front_right_off(leds) :
	GPIO.output(leds[0], False)

def rear_left_on(leds) :
	GPIO.output(leds[2], True)

def rear_left_off(leds) :
	GPIO.output(leds[2], False)

def rear_right_on(leds) :
	GPIO.output(leds[3], True)

def rear_right_off(leds) : 
	GPIO.output(leds[3], False)

def front_light_on(leds):
	front_left_on(leds)
	front_right_on(leds)

def front_light_off(leds):
	front_left_off(leds)
	front_right_off(leds)

def rear_light_on(leds):
	rear_left_on(leds)
	rear_right_on(leds)

def rear_light_off(leds):
	rear_left_off(leds)
	rear_right_off(leds)

def all_light_on(leds):
	front_light_on(leds)
	rear_light_on(leds)

def all_light_off(leds):
	front_light_off(leds)
	rear_light_off(leds)
	
def rear_left_blink(leds):
	for howMany in range(5):
		rear_left_on(leds)
		time.sleep(0.5)
		rear_left_off(leds)
		time.sleep(0.5)
		
def rear_right_blink(leds):
	for howMany in range(5):
		rear_right_on(leds)
		time.sleep(0.5)
		rear_right_off(leds)
		time.sleep(0.5)
