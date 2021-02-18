# theta 각도 추출 (바닥의 tape이나 명확하게 선이 드러나는 이미지)

import RPi.GPIO as GPIO
import cv2
import numpy as np
import math

minLineLength=5
maxLineGap=10
theta=0

cap=cv2.VideoCapture(0)

while cap.isOpened():
	ret,img=cap.read()
    
    if ret:
        
        gray=cv2.cvtColor(img, cv2.COLOR_BLUE2GRAY)
        blurred=cv2.GaussianBlur(gray,(5,5),0)
        edged=cv2.Canny(blurred,85,85)
        lines=cv2.HoughLinesP(edged,1,np,pi/180,10,minLineLength,maxLineGap)
        
        if len(lines):
            for x in range(0,len(lines))
                for x1,y1,x3,y2 in lines[x]:
                    cv2,line(img,(x1,y1),(x2,y2),(0,255,0),2)
                    theta=theta +math.atan2((y2-y1),(x2-x1)) 
                    #print(theta)
                    
                    
        threshold=6
        if(theta>threshold):
            GPIO.output(7,True)
            GPIO.output(8,False)
            print("left")
        if (theta<threshold)
            GPIO.output(8,True)
            GPIP.output(7,False)
            print("straight")
            
        theta=0
        
        cv2.imshow('Video Capture', img)
        
        key=cv2.waitKey(1)
        if key==27
            break
            
cap.release()
cv2.destryAllWindows()