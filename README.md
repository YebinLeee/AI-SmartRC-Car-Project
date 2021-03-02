# AI-SmartRC-Car-Project
A project to make an AI RC Smart Car made by RaspberryPi 3 Model B+, controlled by Linux commands under environments including PuTTY(SSH samba server, python programs-GPIO, OpenCV module) and VNC server(image/video processing).
- Board: Raspberry Pi 3 Model B+
<hr>

<br><br>

<img src="https://github.com/YebinLeee/AI-SmartRC-Car-Project/blob/main/SmartCar-sketch.jpg?raw=true" width="500"></img>

### Files and Downloads

1. Raspberrypi Imager
you need to first download files from here and save the files to your macro storage such as a SD card using Raspberrypi Imager in order to install an environment to use Raspberripy.
You need a card reader in order to read your SD card.

2. other neccessary files
SSH file, config file named wpa_supplicant.conf which includes ssik and psk (ID and PW of your network)

3. PuTTY & Samba protocol server
It is an application that functions as a SSH client. With your own allocated RaspberryPy IP code, you can access through GNU/Linux systems so that you are able to manipulate raspberry py or control GPIO using python or any other program.
You will be using Samba, a server with a networking protocol. It is a service that enables file systems sharing fron Linux to your Wondws disc. You can install a samba server by command lines.

4. VNC viewer
It is a server that allows an user to connect a virtual desktop of raspberrypi to your own PC. You need your Pi's local IP address/pw.

5. python IDE - notepad++
It's your own choice to pick an IDE to use python that allows you to manipulate GPIO, motors, etc.. It depends.

<br><br>


### Raspbian OS Install

1. Download _RaspberryPi Imager_
2. Linux 기반 라즈베리파이 용 _Raspbian OS_ 설치를 위해 [Raspbian images(OS 이미지 lite용)](https://downloads.raspberrypi.org/raspbian_lite/images/) 다운받아
3. 포맷된 상태의 SD카드에 RaspberryPi Imager을 이용해 복사하여 저장

<br>

이 SD 카드에는 필요에 따라 몇 개의 파일이 더 필요하다.
1) _SSH_ 파일 (SSH.text라고 저장한 빈 파일이어도 상관없음) - 원격 접속에 필요한 network protocol
2) _wpa_supplicant.conf_ 파일
- 무선랜으로 접속하는 경우 라즈베리파이가 접속할 수 있는 wifi에 대한 정보를 저장하는 security 파일 
- conf(configuration file 확장자)는 리눅스 기반 환경에서 열 수 있는 텍스트파일을 의미한다.
- [how to set up an wireless LAN?](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)

<br>

### Remote Desktop
1. Download _PuTTY_ - 윈도우에서 SSH protocol을 사용할 수 있도록 제공하는 클라이언트(초기 상태 ID-pi, PW-raspberry)
2. Install _Samba server_
- 윈도우와 리눅스 간의 파일을 공유하기 위한 프로그램
- 윈도우에서 라즈베리파이의 파일 시스템에 접근할 수 있도록 설치
- apt 설치 프로그램 관리자 DB를 업데이트한 후 패키지 

- 삼바 서버 설정까지 끝나면 삼바를 재실행. 재실행해야 설정파일이 적용됨
3. 원격 데스크탑 기능 설정 - 명령어 _sudo apt install xrdp_
4. 윈도우+R키 원격 접속실행 - raspberrypi에 부여된 IP local address 입력하여 접속 (windows에서 파일 쉽게 이용할 수 있음)
