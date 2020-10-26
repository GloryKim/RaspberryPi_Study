# IoTivity Project


## 컴파일 방법
- python dht22.py
-------------------------------------
## 회로 꽂는방법
### 센서 : 번호
1. 형광(저항끼고 가운데) : 7 (GPIO4)
2. 흰색(저항안끼고 바깥 오른쪽) : 17 (3v)
3. 검정(저항안끼고 바깥 왼쪽) : 34 (GND)

-------------------------------------
## dht라이브러리 가져오는 방법
1. cd ..
- 최상단 으로 올라간다.
2. git clone https://github.com/adafruit/Adafruit_Python_DHT.git
- git clone 으로 github에 있는 dht 예제를 가져온다.
3. cd Adafruit_Python_DHT
- Adafruit_Python_DHT 폴더 안에 들어간다.
4. sudo apt-get update
5. sudo apt-get install build-essential python-dev python-openssl
6. sudo python setup.py install
- 여기 까지 완료 했으면 예제를 한번 실행을 시켜본다.
7. cd examples 
- Adafruit_Python_DHT 폴더 안에 있는 examples 폴더 안으로 들어간다.
8. sudo ./AdafruitDHT.py 2302 4
- 여기서 회로 꽂는 방법을 활용하여 회로를 꽂는 다음 컴파일 할때 온도 습도가 한번씩 리턴 되면 OK

-------------------------------------
REF
https://m.blog.naver.com/alkydes/220792520374
https://blog.heeseop.com/122