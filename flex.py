#Flex sensor - Vo = (R^Flex/R+Flex)Vcc, R = 10k
#Rflex 1  = 26, Rflex 2  =32, R =10k, Vcc = 3.3v
from machine import ADC, Pin
import time

#cool like sanvi ray

flex_sensor = ADC(Pin(4))

flex_sensor.atten(ADC.ATTN_11DB)

while True:
    sensor_value = flex_sensor.read()
    print("Flex Sensor Value:", sensor_value)
    time.sleep(0.5)
