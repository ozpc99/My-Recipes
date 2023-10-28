from flask import render_template, request, redirect, url_for
from recipe_site import app, db
from recipe_site.models import Cuisine, Recipe


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/cuisine")
def cuisine():
    cuisines = Cuisine.query.order_by(Cuisine.cuisine_type).all()
    return render_template("cuisine.html", cuisines=cuisines)


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = Cuisine(cuisine_type=request.form.get("cuisine_type"))
        db.session.add(cuisine)
        db.session.commit()
        return redirect(url_for("cuisine"))


@app.route("/edit_cuisine/<int:cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    if request.method == "POST":
        cuisine.cuisine_type = request.form.get("cuisine_type")
        db.session.commit()
        return redirect(url_for("cuisine"))
    return render_template("edit_cuisine.html", cuisine=cuisine)


@app.route("/recipe")
def recipe():
    return render_template("recipe.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")
