from flask import render_template
from recipe_site import app, db


@app.route("/")
def home():
    return render_template("base.html")
