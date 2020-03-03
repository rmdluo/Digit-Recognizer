#gets rid of warnings
import logging
logging.getLogger('tensorflow').disabled = True

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

#load librarys
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, Dropout, MaxPooling2D
from mlxtend.data import loadlocal_mnist
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#variables of data
img_rows = 28
img_cols = 28
num_classes = 10

train_label_file = "data/train-labels-idx1-ubyte"
train_image_file = "data/train-images-idx3-ubyte"

test_label_file = "data/t10k-labels-idx1-ubyte"
test_image_file = "data/t10k-images-idx3-ubyte"

train_x, train_y = loadlocal_mnist(images_path=train_image_file, labels_path=train_label_file)
train_x = train_x.reshape(train_x.shape[0], img_rows, img_cols, 1)
train_x = train_x / 255
train_y = keras.utils.to_categorical(train_y, num_classes)

datagen = ImageDataGenerator(rotation_range=45, width_shift_range=10, height_shift_range=10)
iter = datagen.flow(train_x, train_y)

train_y = keras.utils.to_categorical(train_y, num_classes)

test_x, test_y = loadlocal_mnist(images_path=test_image_file, labels_path=test_label_file)
test_x = test_x.reshape(test_x.shape[0], img_rows, img_cols, 1)
test_x = test_x / 255
test_y = keras.utils.to_categorical(test_y, num_classes)
validation_data = (test_x, test_y)

#batch_size = 10

model = Sequential()

model.add(Conv2D(32, activation="relu", kernel_size=(3, 3), input_shape=(img_rows, img_cols, 1)))
model.add(Conv2D(64, activation="relu", kernel_size=(3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation="softmax"))

model.compile(loss=keras.losses.categorical_crossentropy, optimizer="adam", metrics=["accuracy"])
#model.fit(train_x, train_y, batch_size=128, epochs=10, validation_data=validation_data)

model.fit_generator(iter, epochs=10, validation_data=validation_data)

model.save("model.h5")
