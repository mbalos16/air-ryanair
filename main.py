from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from wtforms import StringField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from form import SearchForm, Register

# Instantiate the app
app = Flask(__name__)


# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)


app.config["SECRET_KEY"] = 'maria'


@app.route("/", methods = ["GET", "POST"])
def home():
    search_form  = SearchForm()
    form_title = "Check the statistics for a flight route"
    return render_template("index.html", form = search_form, form_title = form_title)


@app.route("/about")
def about():
    title = "About Ryanair Radar"
    return render_template("about.html", title = title)


@app.route("/form-response", methods = ["GET", "POST"])
def form_response():
    title = "Form response"
    search_form = SearchForm(request.form)
    if request.method == "POST" and search_form.validate_on_submit():
        depart_iata_code = request.form.get("depart_iata_code")
        arrival_iata_code = request.form.get("arrival_iata_code")
        date_from = request.form.get("date_from")
        date_to = request.form.get("date_to")
        n_passangers = request.form.get("n_passangers")

    return generate_search_results_page(
        depart_iata_code = depart_iata_code, 
        arrival_iata_code = arrival_iata_code, 
        date_from = date_from, 
        date_to=date_to, 
        n_passangers = n_passangers, 
        title = title)


def generate_search_results_page(
    depart_iata_code, arrival_iata_code, date_from , date_to, n_passangers, title):
    
    # Access the database, search the flight and build the history of prices
    
    # Instantiate the tracking form
    register_form = Register()
    
    # Return the rendered page with the form and the history of prices
    return render_template(
        "search_form_response.html", 
        title = title, 
        form = register_form, 
        depart_iata_code = depart_iata_code, 
        arrival_iata_code = arrival_iata_code, 
        date_from = date_from , 
        date_to = date_to, 
        n_passangers = n_passangers)

@app.route("/register_user/<depart_iata_code>-<arrival_iata_code>-<date_from>-<date_to>-<n_passangers>-<title>", methods = ["GET", "POST"])
def register_user_tracking(
    depart_iata_code, arrival_iata_code, date_from , date_to, n_passangers, title):
    if request.method == "POST":
        form  = Register(request.form)
        # Register user to the database
        email = request.form.get("email")
        desired_price = request.form.get("desired_price")
        print(email, desired_price)

        if form.validate_on_submit():
            success = "Your data has been registered successfully. Thank you for joining us! You will now receive a weekly email with your flight statistics."
            return generate_search_results_page(
                depart_iata_code = depart_iata_code, 
                arrival_iata_code = arrival_iata_code, 
                date_from = date_from, 
                date_to=date_to, 
                n_passangers = n_passangers, 
                title = title)

    return render_template("search_form_response.html", 
        title = title, 
        form = register_form, 
        depart_iata_code = depart_iata_code, 
        arrival_iata_code = arrival_iata_code, 
        date_from = date_from , 
        date_to = date_to, 
        n_passangers = n_passangers,
        success = sucess_message)

if __name__ == "__main__":
    app.run(debug = True)