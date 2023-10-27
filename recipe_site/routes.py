from flask import render_template
from recipe_site import app, db
from recipe_site.models import Cuisine, Recipe


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/cuisine")
def cuisine():
    return render_template("cuisine.html")
