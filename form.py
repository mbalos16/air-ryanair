from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired
from datetime import datetime


class SearchForm(FlaskForm):
    depart_iata_code = StringField(
        label = "Departure Airport Code",
        name = "depart_iata_code", 
        render_kw = {
            "placeholder": "Enter IATA code (e. g., STN)..."
        },
        validators = [DataRequired(message = "Please provide a 3-letters IATA Code"), 
            Length(3)])

    arrival_iata_code = StringField(
        label = "Destination Airport Code",
        name = "arrival_iata_code",
        render_kw = {
            "placeholder": "Enter IATA code (e. g., BCN)"
        },
        validators = [DataRequired(message = "Please provide a 3-letters IATA Code"), 
        Length(3)])

    date_from = DateField(
        label = "Depart Date", 
        name = "date_from",
        format='%Y-%m-%d')

    date_to = DateField(
        label = "Return Date",
        name = "date_to",
        format='%Y-%m-%d',)

    n_passangers = IntegerField(
        label = "Passangers", 
        name = "n_passangers",
        default = 1, 
        render_kw = {
            "placeholder": "1"
        },
        validators = [DataRequired()])

    submit_button = SubmitField(
        label = "Get Flight Stats"
    )


class Register(FlaskForm):
    first_name = StringField(
        label = "First Name",
        name = "first_name",
        render_kw = {
            "placeholder": "Maria"
        },
        validators = [DataRequired(message = "Please provide your first name")])

    last_name = StringField(
        label = "Last Name",
        name = "last_name",
        render_kw = {
            "placeholder": "Balos"
        },
        validators = [DataRequired(message = "Please provide your last name")])
    
    email = StringField(
        label = "Email Address",
        name = "email",
        render_kw = {
            "placeholder": "mariabalos16@gmail.com"
        },
        validators = [DataRequired(message = "Please provide your email adress.")])

    depart_iata_code = StringField(
        label = "Departure Airport Code",
        name = "depart_iata_code", 
        render_kw = {
            "placeholder": "Enter IATA code (e. g., STN)..."
        },
        validators = [DataRequired(message = "Please provide a 3-letters IATA Code"), 
            Length(3)])

    arrival_iata_code = StringField(
        label = "Destination Airport Code",
        name = "arrival_iata_code",
        render_kw = {
            "placeholder": "Enter IATA code (e. g., BCN)"
        },
        validators = [DataRequired(message = "Please provide a 3-letters IATA Code"), 
        Length(3)])
    
    submit_button = SubmitField(
        label = "Register"
    )
