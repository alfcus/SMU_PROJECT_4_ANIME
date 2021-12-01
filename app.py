from flask import Flask, render_template, jsonify, send_from_directory, redirect, url_for, request
from random import random
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper

#init app and class
# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

#endpoint
# Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("homepage.html")

# Route to render index.html template
@app.route("/about")
def about():
    # Return template and data
    return render_template("about.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/recommender")
def recommender():
    # Return template and data
    return render_template("recommender.html")

@app.route("/data")
def data():
    # Return template and data
    return render_template("data.html")

@app.route("/resources")
def resources():
    # Return template and data
    return render_template("resources.html")

@app.route("/writeup")
def writeup():
    # Return template and data
    return render_template("writeup.html")

@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    content = request.json["data"]

    # parse
    genre = content["genre"]
    score = float(content["score"])
    animeName = content["animeName"]

    prediction = modelHelper.makePredictions(animeName, genre, score)

    return prediction

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)