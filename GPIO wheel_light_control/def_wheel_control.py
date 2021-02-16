import RPi.GPIO as GPIO

def left_front_forward(dcMotors) :
	GPIO.output(dcMotors[2], True)
	GPIO.output(dcMotors[3], False)

def left_front_backward(dcMotors) :
	GPIO.output(dcMotors[2], False)
	GPIO.output(dcMotors[3], True)

def left_front_stop(dcMotors) :
	GPIO.output(dcMotors[2], False)
	GPIO.output(dcMotors[3], False)

def right_front_forward(dcMotors) :
	GPIO.output(dcMotors[4], True)
	GPIO.output(dcMotors[5], False)

def right_front_backward(dcMotors) :
	GPIO.output(dcMotors[4], False)
	GPIO.output(dcMotors[5], True)

def right_front_stop(dcMotors) :
	GPIO.output(dcMotors[4], False)
	GPIO.output(dcMotors[5], False)

def left_back_forward(dcMotors) :
	GPIO.output(dcMotors[0], True)
	GPIO.output(dcMotors[1], False)

def left_back_backward(dcMotors) :
	GPIO.output(dcMotors[0], False)
	GPIO.output(dcMotors[1], True)

def left_back_stop(dcMotors) :
	GPIO.output(dcMotors[0], False)
	GPIO.output(dcMotors[1], False)

def right_back_forward(dcMotors) :
	GPIO.output(dcMotors[6], True)
	GPIO.output(dcMotors[7], False)

def right_back_backward(dcMotors) : 
	GPIO.output(dcMotors[6], False)
	GPIO.output(dcMotors[7], True)

def right_back_stop(dcMotors) :
	GPIO.output(dcMotors[6], False)
	GPIO.output(dcMotors[7], False)

def go_forward(dcMotors):
	left_front_forward(dcMotors)
	left_back_forward(dcMotors)
	right_front_forward(dcMotors)
	right_back_forward(dcMotors)

def go_backward(dcMotors):
	left_front_backward(dcMotors)
	left_back_backward(dcMotors)
	right_front_backward(dcMotors)
	right_back_backward(dcMotors)

def turn_left(dcMotors):
	left_front_backward(dcMotors)
	left_back_backward(dcMotors)
	right_front_forward(dcMotors)
	right_back_forward(dcMotors)

def turn_right(dcMotors):
	left_front_forward(dcMotors)
	left_back_forward(dcMotors)
	right_front_backward(dcMotors)
	right_back_backward(dcMotors)

def stop_driving(dcMotors):
	left_front_stop(dcMotors)
	left_back_stop(dcMotors)
	right_front_stop(dcMotors)
	right_back_stop(dcMotors)

