# IoTMaskDetectionTempReader
Final project for Internet of Things at the University of Iowa. This software runs on a raspberry pi and utilizes both a thermal camera and a USB camera to detect if a person is using a mask, read their temperature, and upload that data to a database and inform the admin if entry is denied. 

NOTE: To run pipfile and install tensorflow, need to run "sudo apt install libatlas-base-dev" and  "sudo apt-get install python3-h5py" first
Also, the pipenv has issues generating a lock file on RPi with tensorflow.


# Something I've tried (didn't seem to work)
## get a fresh start
sudo apt-get update
sudo apt-get upgrade
## remove old versions, if not placed in a virtual environment (let pip search for them)
pip uninstall tensorflow
pip3 uninstall tensorflow
## install the dependencies (if not already onboard)
sudo apt-get install gfortran
sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev
sudo apt-get install libatlas-base-dev libopenblas-dev libblas-dev
sudo apt-get install openmpi-bin libopenmpi-dev
sudo apt-get install liblapack-dev cython
pip3 install keras_applications==1.0.8 --no-deps
pip3 install keras_preprocessing==1.1.0 --no-deps
pip3 install -U six wheel mock
pip3 install pybind11
pip3 install h5py==2.10.0
## upgrade setuptools 40.8.0 -> 52.0.0
pip3 install --upgrade setuptools
## install gdown to download from Google drive
pip3 install gdown
## copy binairy
POTENTIALLY DON'T NEED: sudo cp ~/.local/bin/gdown /usr/local/bin/gdown
## download the wheel
gdown https://drive.google.com/uc?id=11mujzVaFqa7R1_lB7q0kVPW22Ol51MPg
## install TensorFlow
sudo -H pip3 install tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl
## and complete the installation by rebooting
sudo reboot
