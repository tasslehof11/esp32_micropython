from machine import Pin
from time import sleep_ms

led=Pin(2, Pin.OUT)

while(1):
    led.on()
    print(led.value())
    sleep_ms(500)
    
    led.off()
    print(led.value())
    sleep_ms(500)