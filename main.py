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
    form  = SearchForm()
    form_title = "Check the statistics for a flight route"
    return render_template("index.html", form = form, form_title = form_title)


@app.route("/about")
def about():
    title = "About Ryanair Radar"
    return render_template("about.html", title = title)


@app.route("/register", methods = ["GET", "POST"])
def register():
    form = Register()
    if request.method == "POST":
        form  = Register(request.form)
        if form.validate_on_submit():
            success = "Your data has been registered successfully. Thank you for joining us! You will now receive a weekly email with your flight statistics."
            return render_template('register.html', form = form, success = success)
    return render_template('register.html', form = form,)

@app.route("/form-response", methods = ["GET", "POST"])
def form_response():
    title = "Form response"
    form = SearchForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        depart_iata_code = request.form.get("depart_iata_code")
        arrival_iata_code = request.form.get("arrival_iata_code")
        date_from = request.form.get("date_from")
        date_to = request.form.get("date_to")
        n_passangers = request.form.get("n_passangers")
        # print(depart_iata_code, arrival_iata_code, date_from, date_to, n_passangers)
    return render_template("search_form_response.html", title = title)

if __name__ == "__main__":
    app.run(debug = True)