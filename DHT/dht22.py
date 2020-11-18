import Adafruit_DHT as dht
import threading
import time

def print_dht22():
    h, t =dht.read_retry(dht.DHT22, 4)
    f = (t*9/5)+32
    print 'Fahrenheit={0:0.1f}*F Celsius={1:0.1f}*C Humidity={2:0.1f}%' . format(f, t, h)
    threading.Timer(2.5, print_dht22).start

print_dht22()
