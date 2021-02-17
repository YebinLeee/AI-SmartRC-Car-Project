#컬러 이미지 흑백으로 변환

import cv2

img=cv2.imread('photo.jpg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #BGR형식의 파일을 GRAY형식으로 바꿈 (바이트 데이터의 순서 뒤바뀐것)

cv2.imshow('photo', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()