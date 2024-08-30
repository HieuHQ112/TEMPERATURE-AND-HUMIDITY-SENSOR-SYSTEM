<span style="font-size: 12pt;">  import usocket as socket
except:
  import socket
from machine import Pin
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
ssid = 'Giangnam Coffee'
password = ''
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass
print('Connection successful')
print(station.ifconfig())
led = Pin(13, Pin.OUT)</span>