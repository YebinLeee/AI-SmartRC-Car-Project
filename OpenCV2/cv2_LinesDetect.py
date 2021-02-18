#이미지로부터 선을 추출

import cv2
import numpy as np
import math

minLineLength=5
maxLineGap=10

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
                    
        cv2.imshow('Video Capture', img)
        
        key=cv2.waitKey(1)
        if key==27
            break
            
cap.release()
cv2.destryAllWindows()