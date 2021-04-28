#!/usr/bin/python3

# Imports
import time
import busio
import board
import adafruit_amg88xx
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

# TODO: Initialize Database


# Initialize outputs for green and red leds
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
threshold = 32 #celcius, F = ~90
fever = 38 # F = ~100
green_LED = 27
red_LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(green_LED, GPIO.OUT)
GPIO.setup(red_LED, GPIO.OUT)

# Main loop that runs in a while loop until scan is ready
def main():
    print("test")
    temp = 0
    while temp < 95:
        # TODO: scan for high temp
        sleep(.05)
        temp = 100
    scan_person()


# Collects mask data, temp data, time of day, and determines if entry is allowed. Pushes info to db
def scan_person():
    average_temp = read_average_temp()
    print(average_temp)
    has_mask = check_for_mask()
    allow_entry = True
    if average_temp >= fever or has_mask == False:
        allow_entry = False
    current_time = datetime.now()
    # TODO: Upload current_time, average_temp, has_mask, and allow_entry to database
    if allow_entry:
        GPIO.output(green_LED, GPIO.HIGH)
        sleep(3)
        GPIO.output(green_LED, GPIO.LOW)
    else:
        GPIO.output(red_LED, GPIO.HIGH)
        sleep(3)
        GPIO.output(red_LED, GPIO.LOW)
    main()
    
# TODO: Reads average temperature of hottest point in scan
def read_average_temp():
    average = 0.0
    counter = 0
    for row in amg.pixels:
        for temp in row:
            if temp > threshold:
                average += temp
                counter += 1
    if counter != 0:
        average = average/counter
    return average

# TODO: Reads from camera and determines if scanned person is wearing a mask, returns true if mask is worn, false if not
def check_for_mask():
    return True

if __name__ == "__main__":
    main()

