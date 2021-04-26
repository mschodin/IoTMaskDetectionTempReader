import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import os

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
print(os.path.join(os.getcwd(),  "my_model", "keras_model.h5"))

# Load the model
model = tensorflow.keras.models.load_model(os.path.join(os.getcwd(), "my_model", "keras_model.h5"))

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('test_picture.jpg')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# display the resized image
# image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
# prediction = model.predict(data)
# print(prediction)

cap = cv2.VideoCapture(0)

while(True):
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
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
