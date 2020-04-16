from tensorflow.keras import backend as K
from tensorflow.keras.layers import Input, BatchNormalization, Reshape, ELU
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, MaxPool2D, ZeroPadding2D, Dense, Dropout, Flatten, Activation
from tensorflow.keras.activations import elu
from tensorflow.keras.layers import GRU, Lambda
from tensorflow.keras.optimizers import Adam, RMSprop
import tensorflow as tf

import h5py


class cnn:
    def __init__(self, input_shape, num_genre=10):
        self.input_shape = input_shape
        self.num_genre = num_genre

    def cnn_model(self):
        inpt = Input(shape=self.input_shape)
        x = self.conv_block(inpt, 16)
        x = self.conv_block(x, 32)
        x = self.conv_block(x, 64)
        x = self.conv_block(x, 128)
        x = self.conv_block(x, 256)

        # Global Pooling and MLP
        x = Flatten()(x)
        x = Dropout(0.5)(x)
        x = Dense(512, activation='relu',
                  kernel_regularizer=tf.keras.regularizers.l2(0.02), trainable=False)(x)
        x = Dropout(0.25)(x)
        predictions = Dense(self.num_genre,
                            activation='softmax',
                            kernel_regularizer=tf.keras.regularizers.l2(0.02), trainable=False)(x)

        model = Model(inputs=inpt, outputs=predictions)
        return model

    def conv_block(self, x, n_filters, pool_size=(2, 2)):
        x = Conv2D(n_filters, (3, 3), strides=(1, 1),
                   padding='same', trainable=False)(x)
        x = Activation('relu')(x)
        x = MaxPool2D(pool_size=pool_size, strides=pool_size)(x)
        x = Dropout(0.25)(x)
        return x
