from flask import Flask, request, render_template, session, url_for, redirect
#from flask_cors import CORS, cross_origin
#from flask_wtf import FlaskForm
#from wtforms import TextField, SubmitField
import requests
import asyncio
import joblib
import app_model
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/', methods=('GET', 'POST'))
def Homepage():
    return render_template('homepage.html', name=None)


@app.route('/fileupload', methods=('GET', 'POST'))
def fileupload():
    if request.method == 'POST':
        file1 = request.files['audiofile']
        app_model.upload_audio(file1)
        response = "success"
        return response
    response = "failed"
    return response


@app.route('/viewfile', methods=('GET', 'POST'))
def view_file():
    if request.method == 'GET':
        filename = request.value
        File = app_model.get_file(filename)

    return File


@app.route('/Help', methods=('GET', 'POST'))
def Help():
    return render_template('help.html', name=None)


@app.route('/About', methods=('GET', 'POST'))
def About():
    return render_template('about.html', name=None)


@app.errorhandler(404)
def pagenotfound(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
