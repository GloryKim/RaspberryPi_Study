
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

pin_to_circuit = 35

def rc_time (pin_to_circuit):
    count = 1 #충격을 줄때 1을 리턴

    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)                             
    time.sleep(0.1)
    GPIO.setup(pin_to_circuit, GPIO.IN)

    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count = 1 # 충격 센서는 워낙 단순하게 구성되어있어서 단순히 디지털한 신호밖에 리턴을 안함

    return count


try:

    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
