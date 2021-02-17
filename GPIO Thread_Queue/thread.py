import threading
import time

flag_exit=False


# 첫번째 쓰레드 정의
def t1_main():
    while True:
        print("\tt1")
        time.sleep(0.5)
        if flag_exit: break

# 두번째 쓰레드 생성 정의
def t2_main():
    while True:
        print("\t\tt2")
        time.sleep(0.2)
        if falg_exit: break

# 각 쓰레드 객체 생성 후 시작
t1=threading.Thread(target=t1_main)
t1.start()
t2=threading.Thread(target=t2_main)
t2.start()

# 사용자로부터 입력 받아 출력
try:
    while True:
        userInput =input()
        print(userInput) 

except KeyboardInterrupt:
    pass

# 쓰레드 종료될 때까지 대기
flag_exit=True
t1.join()
t2.join()


t2.join()
