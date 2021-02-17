# 이미지 파일 화면에 출력(VNC viewer의 Terminal이용)

import cv2 #OpenCV 라이브러리 cv2 모듈 불러옴

img=cv2.imread('photo.jpg') #cv2모듈의 imread 호출 - numpy 모듈에서 제공하는 배열 객체 numpy.ndarray 내여줌
# 이 과정 직접 사용자에게 파일명 입력받도록 기능 구현하기

cv2.imshow('photo', img) # 화면에 이미지 표시. 첫번쨰 인수- 화면에 표시되는 제목(변경 가능)
cv2.waitKey(0) # 키보드 입력 대기
cv2.destroyAllWindows() 
