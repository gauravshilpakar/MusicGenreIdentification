from pymongo import MongoClient
import gridfs

client = MongoClient('localhost', 27017)

db = client['database']
fs = gridfs.GridFS(db, "Audio Files")


def upload_audio(audio_file):
    id = fs.put(audio_file, filename=audio_file.filename)
    return id


def get_file(filename):
    File = fs.find_one({"filename": filename})
    return File


def delete_file(id):
    fs.delete(id)
