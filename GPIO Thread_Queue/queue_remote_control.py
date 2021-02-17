# 입력받아 자동차 조작하기 & 전조등 제어 쓰레

import RPi.GPIO as GPIO
from wheel_control import *
from light_control import *
import queue
import threading

HOW_MANY_MESSAGES =10

def blink_led():

	while True:
		msg = mq_blink.get() # 큐 메시지를 받는다
		print("msg:", msg)
		
		if msg=='z':
			rear_left_blink(leds) # 왼쪽 뒤 깜박이
		elif msg=='c':
			rear_right_blink(leds) # 오른쪽 뒤 깜박이
		elif msg=='q':
			break
		
t_blink = threading.Thread(target=blink_led)
t_blink.start()		
    
GPIO.setmode(GPIO.BCM)


dcMotors = [21,18,20,12,22,13,23,19]

for dcMotor in dcMotors:
	GPIO.setup(dcMotor, GPIO.OUT)
	GPIO.output(dcMotor, False)
	
leds = [5,6,7,8]

for led in leds:
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, False)
	
try:
	while True:
		
		print('f:forward, b:backward, l:left, r:right, s:stop')
		print('W/w:front light on/off, U/u:rear light on/off')
		print('A/a:all light on/off')
		print('z:rear left blink, c:rear right blink')
		print('q:quit program')
		
		cmd = input()
		print(cmd)
		if cmd=='q':
			mq_blink.put(cmd)
			t_blink.join()
			break
		
		if cmd=='f':
			go_forward(dcMotors)
		elif cmd=='b':
			go_backward(dcMotors)
		elif cmd=='l':
			turn_left(dcMotors)
			mq_blinkput('z')
		elif cmd=='r':  
			turn_right(dcMotors)
			mq_blink.put('c')
		elif cmd=='s':
			stop_driving(dcMotors)
		
		if cmd=='W':
			front_light_on(leds)
		elif cmd=='w':
			front_light_off(leds)
		elif cmd=='U':
			rear_light_on(leds)
		elif cmd=='u':
			rear_light_off(leds)
		elif cmd=='A':
			all_light_on(leds)
		elif cmd=='a':
			all_light_off(leds)
		elif cmd=='z' or cmd=='c':
			mq_blink.put(cmd)			

except KeyboardInterrupt:
	pass

for dcMotor in dcMotors:
	GPIO.output(dcMotor, False)

for led in leds:
	GPIO.output(led, False)

GPIO.cleanup()

