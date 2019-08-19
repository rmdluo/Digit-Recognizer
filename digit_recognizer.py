#gets rid of warnings
import logging
logging.getLogger('tensorflow').disabled = True

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

#load librarys
import numpy as np
from tensorflow import keras
import cv2

def invert(img):
	for row in range(img.shape[0]):
		for column in range(img.shape[1]):
			if(img[row, column] > 150):
				img[row, column] = 0
			else:
				img[row, column] = 255

filename = input("Enter the filename: ")
img = cv2.imread("numbers/" + filename, 0)

img = cv2.resize(img, (28, 28))
invert(img)

x = img.reshape(1, 28, 28, 1)
x = x / 255

model = keras.models.load_model("model.h5")

pred = model.predict_classes(x)

print(pred)
