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

def findBlankColumn(img):
	for column in range(img.shape[1] // 3, img.shape[1]):
		blank = True
		for row in range(img.shape[0]):
			if(img[row, column] < 150):
				blank = False
		if(blank):
			return column

filename = input("Enter the filename: ")
img = cv2.imread(filename, 0)

column = findBlankColumn(img)
img1 = img[:, :column]
img2 = img[:, column:]


img1 = cv2.resize(img1, (28, 28))
#cv2.imwrite("thing0.jpg", img1)
invert(img1)
#cv2.imwrite("thing1.jpg", img1)

img2 = cv2.resize(img2, (28, 28))
invert(img2)
#cv2.imwrite("thing2.jpg", img2)

x = img1.reshape(1, 28, 28, 1)
x = x / 255

model = keras.models.load_model("model.h5")

pred = model.predict_classes(x)

print(pred)

x = img2.reshape(1, 28, 28, 1)
x = x / 255

model = keras.models.load_model("model.h5")

pred = model.predict_classes(x)

print(pred)
