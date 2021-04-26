# IoTMaskDetectionTempReader
Final project for Internet of Things at the University of Iowa. This software runs on a raspberry pi and utilizes both a thermal camera and a USB camera to detect if a person is using a mask, read their temperature, and upload that data to a database and inform the admin if entry is denied. 


# How to setup python Tensorflow 2 on RPi 4 (32-bit OS)
Use the following download (community TensorFlow binary):
pip3 install https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0-rc2/tensorflow-2.4.0rc2-cp37-none-linux_armv7l.whl

NOTE: If running into errors still, run "sudo apt install libatlas-base-dev" and  "sudo apt-get install python3-h5py"

If trying to use pipfile install with pipenv, lock file will not include tensorflow. It must be downloaded manually. 

## Other things you can download in case it still doesn't work:
### get a fresh start
sudo apt-get update
sudo apt-get upgrade
### install the dependencies (if not already onboard)
sudo apt-get install gfortran
sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev
sudo apt-get install libatlas-base-dev libopenblas-dev libblas-dev
sudo apt-get install openmpi-bin libopenmpi-dev
sudo apt-get install liblapack-dev cython
sudo apt-get install fswebcam
pip3 install keras_applications==1.0.8 --no-deps
pip3 install keras_preprocessing==1.1.0 --no-deps
pip3 install -U six wheel mock
pip3 install pybind11
pip3 install h5py==2.10.0
pip3 install opencv-python
### upgrade setuptools 40.8.0 -> 52.0.0
pip3 install --upgrade setuptools

