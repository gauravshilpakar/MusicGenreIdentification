import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from tenforflow.keras.callbacks import EarlyStopping


class Model():
    # def __init__(self,epoch):
        #self.epoch = epoch

    def create_model(self):
        image_shape = (1920, 1080, 3)
        model = Sequential()
        model = Sequential()
        model.add(Conv2D(filters=32, kernel_size=(3, 3),
                         input_shape=image_shape, activation='relu'))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=64, kernel_size=(3, 3),
                         input_shape=image_shape, activation='relu'))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=64, kernel_size=(3, 3),
                         input_shape=image_shape, activation='relu'))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Flatten())

        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))

        model.add(Dense(8, activation='softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='adam', metrics=['accuracy'])

        early_stop = EarlyStopping(monitor='val_loss', patience=2)

    # def train_model(data):
