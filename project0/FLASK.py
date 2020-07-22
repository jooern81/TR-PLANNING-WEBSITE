# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:24:53 2020

@author: chinjooern
"""

import os

from flask import Flask, session, redirect, render_template, request, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import mysql.connector as mysql
from flask_sqlalchemy import SQLAlchemy
#from models import *






# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DATABASE_URL'] = "postgres://bbilcrjmdqsefb:1792ea62a0f1684cafa24359decd4d31df2ac7f7a2bcf4bf9f86aad8254f5f2f@ec2-35-172-73-125.compute-1.amazonaws.com:5432/d6bt7imri7f5k9"

db = SQLAlchemy(app)

class Consist(db.Model):
    __tablename__ = "Operations"
    id = db.Column(db.Integer, primary_key=True)
    #origin = db.Column(db.String, nullable=False)
    #destination = db.Column(db.String, nullable=False)
    consist_id = db.Column(db.String, nullable=False)


db.create_all()


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/unlimited")
def unlimited():
    return render_template("unlimited_planning_table.html")

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        consist1 = request.form["CONSIST 1"]
        consist = Consist(consist_id = consist1)
        db.session.add(consist)
        db.session.commit()

        return redirect(url_for("consist"))
    else:
        if "consist" in session:
            return redirect(url_for("index"))

        return render_template("completed_works_form.html")


@app.route("/daily")
def daily():
    return render_template("daily_schedule_table.html")


@app.route("/consist")
def consist():
    if "consist" in session:
        consist1 = session["consist"]
        return f"<h1>SUBMITTED</h1>"
    else:
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("consist", None)
    return redirect(url_for("index"))






