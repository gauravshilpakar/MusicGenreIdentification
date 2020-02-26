import numpy as np
import matplotlib.pyplot as plt
import os
from os.path import isfile

import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Flatten, Conv1D, MaxPool1D, BatchNormalization, Lambda
from tensorflow.keras.layers import Input, Dense, TimeDistributed, LSTM, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras import regularizers, Input


class custom_NN():
    def __init__(self):
        self.epoch = 5
        self.batch_size = 32
        self.num_classes = 8
       # self.n_features = X_train.shape[2]
      #  self.n_time = X_train.shape[1]
        self.N_LAYERS = 3
        self.FILTER_LENGTH = 5
        self.CONV_FILTER_COUNT = 56
        self.BATCH_SIZE = 32
        self.LSTM_COUNT = 96
        self.EPOCH_COUNT = 70
        self.NUM_HIDDEN = 64
        self.L2_regularization = 0.001

    def create_model(self):
        input_shape = (None, 128)
        layer = Input(input_shape, name='input')
        for i in range(self.N_LAYERS):
            layer = Conv1D(filters=self.CONV_FILTER_COUNT,
                           kernel_size=self.FILTER_LENGTH, activation='relu')(layer)
            layer = MaxPool1D(pool_size=2)(layer)
            layer = Dropout(0.4)(layer)

        #layer = Flatten()(layer)
        # LSTM Layer
        layer = LSTM(self.LSTM_COUNT, return_sequences=False)(layer)
        layer = Dropout(0.4)(layer)

        # Dense Layer
        layer = Dense(128, activation='relu', name='Dense1')(layer)
        layer = Dropout(0.5)(layer)

        # output layer
        layer = Dense(8, activation='softmax', name='Dense2')(layer)

        model_input = Input(input_shape, name='input')
        model_output = layer

        model = Model(model_input, model_output)
        model.compile(loss='categorical_crossentropy',
                      optimizer='adam', metrics=['accuracy'])

        early_stop = EarlyStopping(monitor='val_loss', patience=2)

        return model

    def train_model(self, X_train, y_train, X_val, y_val):
        model = self.create_model()
        model.fit(X_train, y_train, batch_size=self.BATCH_SIZE,
                  epochs=self.EPOCH_COUNT, validation_data=(X_val, y_val), verbose=1)


if __name__ == '__main__':
    custom_model = custom_NN()
    model = custom_model.create_model()
