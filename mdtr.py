#!/usr/bin/python3

# General Lifecycle Imports
from time import sleep
from datetime import datetime
# RPi Output Pin Imports
import RPi.GPIO as GPIO
# Mask Detection Camera Imports
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import os

# TODO: Initialize Database


# Initialize outputs for green and red leds
# TODO: Change pin below to correct pin
green_LED = 18
red_LED = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setup(green_LED, GPIO.OUT)
GPIO.setup(red_LED, GPIO.OUT)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
# Load the model
model = tensorflow.keras.models.load_model(os.path.join(os.getcwd(), "my_model", "keras_model.h5"))
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Resize the image to a 224x224 with the same strategy as in TM2:
# Resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
# Initialize camera 
cap = cv2.VideoCapture(0)

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
    has_mask = 0
    for x in range(0,30):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(frame, size, interpolation = cv2.INTER_AREA)

        # Normalize the image
        normalized_image_array = (resized.astype(np.float32) / 127.0) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        prediction = model.predict(data)
        if prediction == 'Mask':
            has_mask += 1
            
    return True if has_mask >= 15 else False

if __name__ == "__main__":
    main()

