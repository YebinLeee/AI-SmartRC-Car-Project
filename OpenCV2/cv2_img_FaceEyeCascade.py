# OpenCV를 이용한 얼굴의 측면 인식(얼굴+눈 인식)
# haarcascade_eye.xml 파일 추가 (https://github.com/opencv/opencv/data/haarcascade/ haarcascade_eye.xml)
import cv2

img=cv2.imread('photo.jpg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

faces=face_cascade.detectMultiScale(gray,1.3,5)
for(x,y,w,h) in faces:
	img=cv2.rectangle(img,(x,y),(x +w, w, +h), (255,0,0),2)
	roi_gray=gray[y:y +h, x:x +w]
	roi_color=img[y:y +h, x:x +w]
	eyes=eye_cascade,detectMultiScale(roi_gray)
	for(ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex +ew,ey +eh),(0,255,0),2)
		

cv2=imshow('photo',img)
cv2.waitKey(0)
cv2.destroyAllWindows
