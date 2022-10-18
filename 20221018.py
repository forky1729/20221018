import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [21,20,16,12,7,8,25,24]
GPIO.setup(leds, GPIO.OUT)

dac = [26,19,13,6,5,11,9,10]
GPIO.setup(dac,GPIO.OUT)

comp = 4
GPIO.setup(comp, GPIO.IN)

troyka = 17
GPIO.setup(troyka, GPIO.OUT)


bits = len(dac)
levels = 2**bits
maxV = 3.3



def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def n2d(value):
    signal = d2b(value)
    GPIO.output(led, signal)
    return signal

def adc():
    for value in range (256):
            signal = n2d(value)
            time.sleep(0.0007)
            compV = GPIO.input(comp)
            if compV == 0:
                return value
                break

try:
    while True:
        print(adc()*3.3/256)
finally:
    GPIO.output(led, [0,0,0,0,0,0,0,0])

s = time.time()
