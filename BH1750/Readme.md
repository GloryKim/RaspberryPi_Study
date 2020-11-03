# IoTivity Project


## 컴파일 방법
- python bh1750.py
-------------------------------------
## 회로 꽂는방법
### 센서 : 번호
1. VCC : 1 (3V)
2. GND : 6 (GND)
3. SDA : 3 (BCM2(SDA))
4. SCL : 5 (BCM3(SCL))

-------------------------------------
## 환경설정
1. sudo raspi-config
- i2c 관련 툴과 라이브러리들은 라즈베리파이에 이미있다.
- 하지만 실제 라즈베리파이 i2c 통신 라인은 비활성화 되어있다.
- i2c 통신 라인을 활성 시켜주자
2. Interfacing Options | Configure connections to peripherals 엔터
3. I2C | Enalbe/Disable sutomatic loading of I2C kernel module 엔터
4. Yes 엔터
5. Finish 엔터
6. sudo reboot
7. 재부팅
8. ls /dev/i2c*
- 작성시 노란 글씨로 /dev/i2c-1 나오면 ㅇㅋ
9. i2cdetect -y 1
- 만약에 0x23 번지에 23이라고 뜨면 연결 된거임
- 만약에 안되면 케이블 문제, 센서 문제, 접촉 불량임

-------------------------------------
## 소스코드 다운로드
1. 다운로드 받을 파일 안쪽을 cd를 이용해서 들어가기
2. wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bh1750.py
3. python bh1750.py
4. python3 bh1750.py
5. 3번 4번 둘중 하나로 실행 가능

-------------------------------------
### 출처
1. https://learn.adafruit.com/adafruit-bh1750-ambient-light-sensor/python-circuitpython
2. https://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/
3. https://m.blog.naver.com/PostView.nhn?blogId=chandong83&logNo=221603593417&proxyReferer=https:%2F%2Fwww.google.com%2F