#아무것도 안만지면 출력이 전혀 없음
#만지길 시작하면 0이상의 값을 0.1초 간격으로 출력함

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

# 35번 핀을 사용함
pin_to_circuit = 35

def rc_time (pin_to_circuit):
    count = 0

    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
 
                                            
    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN)

 
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count


try:

    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
