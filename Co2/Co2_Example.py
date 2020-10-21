import RPi.GPIO as GPIO 
import time# sleep
GPIO.setmode(GPIO.BOARD)
# GPIO.BOARD 보드 상의 핀 번호 사용
# GPIO.BCM .  핀번호가 아니라 Broadcom SOC channel을 사용 GPIOXX의 XX 번호를 사용

# 35번 핀을 사용함
pin_to_circuit = 35

def rc_time (pin_to_circuit):
    count = 0

    #Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)   # 35번 핀을 입력으로 설정
    GPIO.output(pin_to_circuit, GPIO.LOW)  # 35번 핀의 디지털 출력 설정
 
                                                      
    time.sleep(0.1)  # 0.1 sec sleep

    # 35번 핀을 input으로 변경
    GPIO.setup(pin_to_circuit, GPIO.IN)

    # 35번 핀으로부터 읽은 값이 HIGH가 될 때까지 count 수행
    # 그래서 실행해보면 센서 주변이 어두울 수록 카운트 값이 크다. 
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count


# 스크립트가 인터럽트 될때 catch하고, 올바르게 cleanp
try:
    # 메인 루프
    while True:
        print rc_time(pin_to_circuit) # 조도 센서의 값 출력
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # 사용했던 모든 포트에 대해서 정리