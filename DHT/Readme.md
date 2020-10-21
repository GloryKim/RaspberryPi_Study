# IoTivity Project


## 컴파일 방법
- sudo gcc –o dht22+while1 dht22+while1.c –lwiringPi
- sudo ./dht22+while1
-------------------------------------
## 회로 꽂는방법
### 센서 : 번호
1. 형광(저항끼고 가운데) : 7 (GPIO4)
2. 흰색(저항안끼고 바깥 오른쪽) : 17 (3v)
3. 검정(저항안끼고 바깥 왼쪽) : 34 (GND)