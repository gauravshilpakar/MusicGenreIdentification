import datetime
import sys
import os
import uuid
from datetime import datetime, timezone

import firebase_admin
from firebase_admin import credentials, firestore, storage

from db_research.yt_download import ytdownload
from models.model_app import PredictModel


COLLECTION = "mfcc"
PATH = os.path.join("db_research/")
cred = credentials.Certificate(os.path.join(PATH, 'secrets.json'))
default_app = firebase_admin.initialize_app(cred,
                                            {'storageBucket': 'python-db-test-62886.appspot.com'})
db = firestore.client()
bucket = storage.bucket()
imageBlob = bucket.blob("/")


class mfcc_file():
    def __init__(self, _id=str(uuid.uuid4()),
                 link=None,
                 link_prediction=None,
                 datetime=str(datetime.now(timezone.utc))[:19],
                 name=None,
                 predictedGenre=None):
        self._id = str(uuid.uuid4())
        self.link = link
        self.link_prediction = link_prediction
        self.datetime = datetime
        self.name = name
        self.predictedGenre = predictedGenre

    def add_data(self, link):
        aud_file = ytdownload(link)
        # print(aud_file)
        aud_file += ".mp4"

        message, img_file, prediction, self.predictedGenre = PredictModel(
            aud_file)
        self.name = img_file.split("_")[0]
        print("DONE")
        output_path = os.path.join('spectral_output/')
        imageBlob = bucket.blob("spectral_output/" + self._id + "_img.png")
        with open(output_path + img_file, 'rb') as img:
            imageBlob.upload_from_file(img,
                                       content_type='image/png')
        self.link = imageBlob.public_url

        output_path_prediction = os.path.join('prediction_output/')

        imageBlob_predictions = bucket.blob(
            "output_path_prediction/" + self._id + "_prediction.png")
        with open(output_path_prediction + prediction, 'rb') as img:
            imageBlob_predictions.upload_from_file(img,
                                                   content_type='image/png')
        self.link_prediction = imageBlob_predictions.public_url

        doc_ref = db.collection(f'{COLLECTION}').document(f'{self._id}')
        doc_ref.set({
            u'_id': f'{self._id}',
            u'name': f'{self.name}',
            u'link': f'{self.link}',
            u'link_prediction': f'{self.link_prediction}',
            u'datetime': f'{self.datetime}',
            u'predictedGenre': f'{self.predictedGenre}'
        })
        print("Successfully uploaded to DB.")
        print(f"{self.link}")

        return self.name, message, self.link, self.link_prediction


def print_db():
    users_ref = db.collection(f'{COLLECTION}')
    docs = users_ref.stream()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


def main(inp_link):
    f = mfcc_file()
    link = inp_link
    vid_title, message, mfcc_link, prediction = f.add_data(link)
    return vid_title, message, mfcc_link, prediction
