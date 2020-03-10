import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import librosa


from os.path import isfile

import tensorflow as tf
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, Flatten, Conv1D, MaxPool1D, BatchNormalization, Lambda
from tensorflow.keras.layers import Input, Dense, TimeDistributed, LSTM, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras import regularizers, Input
#from tensorflow.python.estimator.model_fn import Modekeys as Modes

from sklearn.metrics import classification_report, confusion_matrix

epoch = 5
batch_size = 32
num_classes = 8
# n_features = X_train.shape[2]
#  n_time = X_train.shape[1]
N_LAYERS = 3
FILTER_LENGTH = 5
CONV_FILTER_COUNT = 56
BATCH_SIZE = 32
LSTM_COUNT = 96
EPOCH_COUNT = 10
NUM_HIDDEN = 64
L2_regularization = 0.001

dict_genres = {'Electronic': 0, 'Experimental': 1, 'Folk': 2, 'Hip-Hop': 3,
               'Instrumental': 4, 'International': 5, 'Pop': 6, 'Rock': 7}


def model_fn(input_shape):
    model_input = Input(input_shape, name='input')
    layer = model_input
    for i in range(N_LAYERS):
        layer = Conv1D(filters=CONV_FILTER_COUNT,
                       kernel_size=FILTER_LENGTH, activation='relu', kernel_regularizer=regularizers.l2(0.001))(layer)
        layer = BatchNormalization(momentum=0.9)(layer)
        layer = MaxPool1D(pool_size=2)(layer)
        layer = Dropout(0.3)(layer)

    # LSTM Layer
    layer = LSTM(LSTM_COUNT, return_sequences=False)(layer)
    layer = Dropout(0.4)(layer)

    # Dense Layer
    layer = Dense(NUM_HIDDEN, kernel_regularizer=regularizers.l2(
        0.001), name='Dense1')(layer)
    layer = Dropout(0.4)(layer)

    # output layer
    layer = Dense(8, activation='softmax', name='Dense2')(layer)
    model_output = layer

    model = Model(model_input, model_output)
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])

    early_stop = EarlyStopping(monitor='val_loss', patience=2)

    return model


def train_model(X_train, y_train, X_val, y_val):
    input_shape = (None, 128)
    model = model_fn(input_shape)
    model.fit(X_train, y_train, batch_size=BATCH_SIZE,
              epochs=EPOCH_COUNT, validation_data=(X_val, y_val), verbose=1)
    model.save('genre_predictor/models/mymodel1.h5')


if __name__ == '__main__':

    # training_file = np.load('genre_predictor/Data/shuffled_train.npz')
    # X_train, y_train = training_file['arr_0'], training_file['arr_1']
    # val_file = np.load('genre_predictor/Data/shuffled_valid.npz')
    # X_val, y_val = val_file['arr_0'], val_file['arr_1']

    test_data = np.load('genre_predictor/Data/test_arr.npz')
    X_test, y_test = test_data['arr_0'], test_data['arr_1']

    # train_model(X_train, y_train, X_val, y_val)
    new_model = load_model('genre_predictor/models/mymodel1.h5')

    y_test -= 1

    X_test_raw = librosa.core.db_to_power(X_test, ref=1.0)
    X_test = np.log(X_test_raw)

    y_pred = new_model.predict(X_test)
    y_pred = np.argmax(y_pred, axis=1)
    #print(classification_report(y_pred, y_test, target_names=dict_genres.keys()))
    mat = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(16, 5))
    sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
                xticklabels=dict_genres.keys(),
                yticklabels=dict_genres.keys(), linewidths=.5)
    plt.xlabel('true label')
    plt.ylabel('predicted label')
    plt.show()
