# 카메라 영상 저장하기

import cv2

cap=cv2.VideoCapture(0) # VideoCapture 클래스의 객체 생성

#영상 입력 기능이 정상적으로 열린 경우
if cap.isOpened():

    # 영상의 가로, 세로, 초당 프레임 수를 변수에 저장
    w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps=int(cap.get(cv2.CAP_PROP_FPS))
    
    fourcc=cv2.VideoWriter_fourcc(*'DIVX')
    # VideoWriter_fourcc 함수 호출하여 fourcc 코드를 받음(=영상 파일 저장 DIVX 형식)
    #D, I, V, X 문자열을 각각의 문자로 나누어 인자로 넘김
    
    out=cv2.VideoWriter('output.avi', fourcc, fps, (w,h))
    # 인수 : 영상 파일명, 영상 파일 저장 형식, 초당 저장할 프레임수, 해상도

while cap.isOpened():
    ret,img=cap.read() # 비디오 프레임 읽어옴
    
    if ret:
        cv2.imshow('Video Capture', img) # 화면에 출력
        
        out.write(img) # out변수가 가리키는 파일에 저장
        
        k=cv2.waitKey(1)
        if k==27:
            break
            
out.release()
cap.release()
cv2.destroyAllWindows()