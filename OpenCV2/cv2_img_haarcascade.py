# haarcascade_frontalface_default.xml 파일 이용해 얼굴 인식

import cv2

img=cv2.imread('photo.jpg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 흑백으로 변환



face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cv2 모듈의 CascadeClassifier 클래스 이용해 객체 생성 (파일명 인수로 전달)
# CascadeClassifier - 머신 러닝 기반의 객체 검출 알고리즘 구현한 클래스

faces=face_cascade.detectMultiScale(gray,1.3,5)
# 생성한 객체에 대해 detectMultiScale 함수 호출하여 얼굴 검출
# 입력된 그림을 내부적으로 축소해가며 검출함. 파일을 해당 비율만큼 반복적으로 줄여감(1.3배만큼 줄임 - 30%)
# 값과 검출율은 반비례
# 5 인수값 - 축소과정 반복하며 최소 5회 검출되었을  얼굴로 인식

# 좌표와 크기에 대해 그림 파일에 사각형 표시 추가함
for(x,y,w,h) in faces:
    img=cv2.rectangle(img,(x,y),(x +w, y +h), (255,0,0,),2)
    
cv2.imshow('photo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()