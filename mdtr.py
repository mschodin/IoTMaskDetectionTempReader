#!/usr/bin/python3

# Imports
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

# TODO: Initialize Database


# Initialize outputs for green and red leds
# TODO: Change pin below to correct pin
green_LED = 18
red_LED = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setup(green_LED, GPIO.OUT)
GPIO.setup(red_LED, GPIO.OUT)

# Main loop that runs in a while loop until scan is ready
def main():
    temp = 0
    while temp < 95:
        # TODO: scan for high temp
        sleep(.05)
        temp = 100
    scan_person()


# Collects mask data, temp data, time of day, and determines if entry is allowed. Pushes info to db
def scan_person():
    average_temp = read_average_temp()
    has_mask = check_for_mask()
    allow_entry = True
    if average_temp >= 100 or has_mask == False:
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
    return 101

# TODO: Reads from camera and determines if scanned person is wearing a mask, returns true if mask is worn, false if not
def check_for_mask():
    return False

if __name__ == "__main__":
    main()

