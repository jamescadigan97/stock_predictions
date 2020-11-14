#Import dependencies
import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, redirect



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

@app.route("/limitations") 
def limitations():

    return render_template("Limitations.html")

@app.route("/about") 
def about():

    return render_template("About.html")



if __name__ == '__main__':
    app.run(debug=True)
