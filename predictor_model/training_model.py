from custom_cnn import cnn
import numpy as np
from audio_processing import make_dataset_dl, majority_voting

X = make_dataset_dl(
    'E:/Texas Tech University/Spring 2020/ECE-3334/Data/genres/blues/blues.00000.wav')

genres = {
    'metal': 0, 'disco': 1, 'classical': 2, 'hiphop': 3, 'jazz': 4,
    'country': 5, 'pop': 6, 'blues': 7, 'reggae': 8, 'rock': 9
}


customModel = cnn(input_shape=(128, 129, 1))
model = customModel.cnn_model()
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.load_weights('genre_predictor\models\weights.h5',
                   by_name=True)
preds = model.predict(X)
votes = majority_voting(preds, genres)
print("Input song is a {} song".format(votes[0][0]))
print("most likely genres are: {}".format(votes[:3]))
