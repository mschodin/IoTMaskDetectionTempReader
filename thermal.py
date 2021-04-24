# sudo pip3 install adafruit-circuitpython-amg88xx
# sudo raspi-config
#       Select "Interfacing Options" -> Select "I2C" -> Select "Yes" -> Select "OK" if applicable -> Appply changes and restart Pi

import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)


threshold = 32 #celcius, F = ~90
fever = 38 # F = ~100

while True:
    average = 0.0
    counter = 0
    for row in amg.pixels:
        for temp in row:
            if temp > threshold:
                average += temp
                counter += 1
    if counter != 0:
        average = average/counter
        print(average)
        if average >= fever:
            print("fever")
        print("\n")
    time.sleep(1)
