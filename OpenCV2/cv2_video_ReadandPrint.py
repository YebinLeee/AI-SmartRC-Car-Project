# 파일 영상 읽고 출력
import cv2
cap=cv2.VideoCapture('output.avi')

if cap.isOpened():

    print('width:',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print('height:',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('fps:',cap.get(cv2.CAP_PROP_FPS))
	
while cap.isOpened():
    ret,img=cap.read()
    
    if ret:
        cv2.imshow('Video Capture', img)
        
        k=cv2.waitKey(30) # 30ms wait 
        if k==27:
            break
    else: break

cap.release()
cv2.destroyAllWindows()