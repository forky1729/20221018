import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)

dac = [26,19,13,6,5,11,9,10]
leds = [21,20,16,12,7,8,25,24]
comp = 4
troyka = 17

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def n2d(value):
    signal = d2b(value)
    GPIO.output(dac, signal)
    return signal

def adc1():
    for value in range (256):
            n2d(value)
            time.sleep(0.01)
            compV = GPIO.input(comp)
            if compV == 0:
                return value
                break

try:
    res = []
    s_t = time.time()
    v = 3
    GPIO.output(troyka, v)
    while adc1()*3.3/256<1.04:
        print(adc1()*3.3/256)
        res.append(adc1()*3.3/256)
    GPIO.output(troyka, 0)
    while adc1()*3.3/256>0.1:
        print(adc1()*3.3/256)
        res.append(adc1()*3.3/256)
    f_t = time.time()
finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])

print("Time = ", f_t - s_t)
print("Period = ", (f_t - s_t)/len(res))

res_str = [str(item) for item in res]

with open("data.txt", "w") as outfile:
    outfile.write("\n".join(res_str))

plt.plot(res)
plt.show()
