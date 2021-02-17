# 라즈베이파이 카메라로부터 영상 받아 화면에 출력

import cv2

cap=cv2.VideoCapture(0) #카메라의 번호(1대를 의미)

#영상 입력 기능이 정상적으로 열린 경우
if cap.isOpened():
    
    # 영상의 가로, 세로, 초당 프레임 수 출력
    print('width:',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print('height:',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('fps:',cap.get(cv2.CAP_PROP_FPS))
    

while cap.isOpened():
    ret,img=cap.read() # 비디오 프레임을 읽어옴. 정상적으로 읽히면 True, 아니면 False값(그림에 대한 행렬 객체 받음)
    
    if ret:
        cv2.imshow('Video Capture', img) #화면에 보여줌(Video Capture 인수 - 영상의 제목)
        
        key=cv2.waitKey(1) &0xFF #1밀리 초간 키보드 입력 기다림
        if key==27: #ESC값인 경우엔 빠져나옴
            break
 
cap.release()
cv2.destryAllWindows()