import Adafruit_DHT as dht
import threading
import time

def print_dht22():
    h, t =dht.read_retry(dht.DHT22, 4)
    print 'Temp={0:0.lf}*C Humidity={1:0.lf}%' . format(t, h)
    threading.Timer(2.5, print_dht22).start

print_dht22()