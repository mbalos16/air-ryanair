from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm #CSRFProtect
from wtforms import StringField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from datetime import datetime


# Instantiate the app
app = Flask(__name__)


# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)


class SearchForm(FlaskForm):
    iata_from = StringField(
        label = "Departure Iata Code", 
        validators = [DataRequired(message = "Please provide a 3-letters IATA Code"), 
            Length(3)])
    iata_to = StringField(
        label = "Arrival Iata Code", 
        validators = [DataRequired(message = "Please provide a 3-letters IATA Code"), 
        Length(3)])

    date_from = DateField(
        label = "Date From", 
        format='%Y-%m-%d',
        validators = [Length(6)])
    date_to = DateField(
        label = "Date To", 
        format='%Y-%m-%d',
        validators = [Length(6)])
    n_adults = IntegerField(
        label = "Number ofAdults", 
        default = 1, 
        validators = [DataRequired()])


@app.route("/", methods = ["GET", "POST"])
def home():
        return render_template("index.html")


if __name__ == "__main__":
    app.run()