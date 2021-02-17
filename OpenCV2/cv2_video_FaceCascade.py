# 카메라 영상 얼굴 인식

import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 얼굴 검출에 필요한 객체 생성

cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,img=cap.read()
    
    if ret:
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 흑백 BGR 형식으로 변환
        faces=face_cascade.detectMultiScale(gray,1.3,5) # 얼굴 검출. 입력된 그림 축소해가며 검출 대상을 검출 (5번까지 실행 후 판단)
        for(x,y,w,h) in faces:
            img=cv2.rectangle(img,(x,y),(x +w, y +h),(255,0,0),2)
            
        cv2.imshow('Video Capture', img)
        
        key=cv2.waitKey(1)
        if key==27:
            break

cap.release()
cv2.destroyAllWindows