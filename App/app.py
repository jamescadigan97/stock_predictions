#Import dependencies
import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, redirect
from csco_prediction import csco1


app = Flask(__name__)

@app.route("/") 
def welcome():

    return render_template("index.html")

@app.route("/CSCO") 
def CSCO():

    return render_template("CSCO.html")

@app.route("/EDU") 
def EDU():

    return render_template("EDU.html")

@app.route("/LSTM") 
def limitations():

    return render_template("LSTM.html")

@app.route("/train") 
def about():

    return render_template("train.html")


@app.route("/predict") 
def app_code():

    csco1()
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)
