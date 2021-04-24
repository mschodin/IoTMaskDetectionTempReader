# IoTMaskDetectionTempReader
Final project for Internet of Things at the University of Iowa. This software runs on a raspberry pi and utilizes both a thermal camera and a USB camera to detect if a person is using a mask, read their temperature, and upload that data to a database and inform the admin if entry is denied. 

NOTE: To run pipfile and install tensorflow, need to run "sudo apt install libatlas-base-dev" first
Also, the pipenv has issues generating a lock file on RPi with tensorflow.