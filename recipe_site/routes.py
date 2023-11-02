from flask import render_template, request, redirect, url_for
from recipe_site import app, db
from recipe_site.models import Cuisine, Recipe


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/cuisine")
def cuisine():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
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


@app.route("/delete_cuisine/<int:cuisine_id>")
def delete_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    db.session.delete(cuisine)
    db.session.commit()
    return redirect(url_for("cuisine"))


@app.route("/recipes")
def recipes():
    recipes = Recipe.query.order_by(Recipe.id).all()
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    return render_template("recipes.html", recipes=recipes, cuisines=cuisines)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            cuisine_id=request.form.get("cuisine_id"),
            recipe_description=request.form.get("recipe_description"),
            recipe_serves = request.form.get("recipe_serves"),
            recipe_ingredients = request.form.get("recipe_ingredients"),
            recipe_method = request.form.get("recipe_method"),
            # recipe_img = ,
            # author_name = ,
            post_date=request.form.get("post_date")
            # is_featured=bool(True if request.form.get("is_featured") else False),
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("recipes"))
    return render_template("add_recipe.html", cuisines=cuisines)


@app.route("/recipe")
def recipe():
    recipes = Recipe.query.order_by(Recipe.id).all()
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    return render_template("recipe.html", recipes=recipes, cuisines=cuisines)
