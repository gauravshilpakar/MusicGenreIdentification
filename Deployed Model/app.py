import os
import sys

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

from db_research.main import main as mfcc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

__package__ = None
@app.route('/', methods=['GET', 'POST'])
@app.route("/ytlink", methods=['GET', 'POST'])
def yt_link():
    if request.method == "POST":
        link = request.form["nm"]
        vid_title, message, mfcc_link, prediction = mfcc(link)

        flash(f"Link Received: {link}", category="info")
        flash(f"Title: {vid_title}", category="info")
        flash(f"{message}\n")
        return render_template('ytpage.html', mfcc_link=mfcc_link, prediction_link=prediction)
    else:
        return render_template('ytpage.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=80)
    # app.run(debug=True)
