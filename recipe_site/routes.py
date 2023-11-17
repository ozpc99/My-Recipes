from flask import (
    render_template,
    request,
    redirect,
    url_for,
    abort,
    g,
    session,
    flash)
from functools import wraps
from sqlalchemy import func, or_
from sqlalchemy.orm.attributes import flag_modified
from datetime import datetime
from recipe_site import app, db
from recipe_site.models import Cuisine, Recipe, User


# Gets today's date and returns value as date
def get_todays_date():
        today = datetime.today()
        return today


# Gets session user's id and assigns it to the 'g.user' global variable
@app.before_request
def load_user():
    user_id = session.get('user_id')
    g.user = User.query.get(user_id) if user_id is not None else None
    print(f"load_user - g.user: {g.user}")


# === Home Page ===
# (renders template: 'base.html' + home page block content)
@app.route("/")
def home():
    recipes = Recipe.query.order_by(Recipe.id).all()
    for recipe in recipes:
        if recipe.average_rating is None:
            recipe.average_rating = 0
    return render_template("base.html", recipes=recipes)


# === Search Results ===
# (renders template: 'results.html')
@app.route("/results", methods=["GET"])
def results():
    search_value = request.args.get('search_value')
    matching_recipes = Recipe.query.filter(
        or_(Recipe.recipe_name.ilike(f"%{search_value}%"),
            Recipe.recipe_description.ilike(f"%{search_value}%"))).all()
    if not matching_recipes:
        flash("Sorry, we couldn't find what you were looking for", "secondary")
    return render_template("results.html", recipes=matching_recipes)


# === Sign Up Form ===
# (renders template: 'sign_up.html')
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        f_name = request.form.get("f_name")
        l_name = request.form.get("l_name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        mailing_list = request.form.get("mailing_list") == "on"
        # checks if 'password' matches 'confirm_password'
        if password != confirm_password:
            return redirect(url_for("sign_up"))
        # checks if the username is already taken
        if User.query.filter_by(username=username).first():
            return redirect(url_for("sign_up"))
        user = User(
            f_name=f_name,
            l_name=l_name,
            email=email,
            username=username,
            password=password,
            mailing_list=mailing_list
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("sign_up.html")


# === Sign In Form ===
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(
            username=username,
            password=password).first()

        if user:
            session["user_id"] = user.id
            g.user = user
            print(f"sign_in - g.user: {g.user}")
            return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
    return redirect(url_for("home"))


# === Sign Out Button ===
@app.route("/sign_out")
def sign_out():
    session.pop("user_id", None)
    return redirect(url_for("home"))


# === Reset Password Form ===
@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        new_password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if passwords match
        if new_password != confirm_password:
            return redirect(url_for("reset_password"))

        # Find the user by email or username
        user = User.query.filter(
            (User.email == email) | (User.username == username)).first()

        if user:
            # Update the user's password
            user.password = new_password
            db.session.commit()
            return redirect(url_for("home"))
        # else:
    return render_template("reset_password.html")


# === Cuisine Categories ===
# (returns template: 'cuisine.html')
@app.route("/cuisine")
def cuisine():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    return render_template("cuisine.html", cuisines=cuisines)


# === Add Cuisine Form ===
@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = Cuisine(
            cuisine_type=request.form.get("cuisine_type"),
            cuisine_img=request.form.get("cuisine_img"),
            user_id=session.get("user_id"))
        db.session.add(cuisine)
        db.session.commit()
        return redirect(url_for("cuisine"))


# === Edit Cuisine Form ===
@app.route("/edit_cuisine/<int:cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    if request.method == "POST":
        cuisine.cuisine_type = request.form.get("cuisine_type")
        db.session.commit()
        return redirect(url_for("cuisine"))


# === Delete Cuisine Form ===
@app.route("/delete_cuisine/<int:cuisine_id>")
def delete_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    db.session.delete(cuisine)
    db.session.commit()
    return redirect(url_for("cuisine"))


# === Recipes ===
# (returns template: 'recipes.html')
# Displays recipes based on cuisine_type: 'recipe.cuisine'
@app.route("/recipes")
def recipes():
    cuisine_id = request.args.get("cuisine_id")
    if cuisine_id:
        recipes = Recipe.query.filter_by(
            cuisine_id=cuisine_id).order_by(Recipe.id).all()
        cuisine = Cuisine.query.get(cuisine_id)
        cuisine_type = cuisine.cuisine_type
    else:
        recipes = Recipe.query.order_by(Recipe.id).all()
        cuisine_type = "All Cuisines"

    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    return render_template(
        "recipes.html",
        recipes=recipes,
        cuisines=cuisines,
        cuisine_type=cuisine_type)


# === Recipe ===
# (returns template: 'recipe.html')
# Displays recipe for recipe_id: 'recipe.id'
@app.route("/recipe/<int:id>")
def recipe(id):
    recipe = Recipe.query.get(id)
    return render_template("recipe.html", recipe=recipe)


# === Add Recipe Form ===
# (returns template: 'add_recipe.html')
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    cuisines = Cuisine.query.order_by(Cuisine.cuisine_type).all()
    if request.method == "POST":
        recipe_name = request.form.get("recipe_name")
        cuisine_id = request.form.get("cuisine_id")
        recipe_description = request.form.get("recipe_description")
        recipe_serves = request.form.get("recipe_serves")
        recipe_ingredients = request.form.get("recipe_ingredients")
        recipe_method = request.form.get("recipe_method")
        recipe_img = request.form.get("recipe_img")
        user_id = session.get("user_id")
        post_date = get_todays_date()
        recipe = Recipe(
            recipe_name=recipe_name,
            cuisine_id=cuisine_id,
            recipe_description=recipe_description,
            recipe_serves=recipe_serves,
            recipe_ingredients=recipe_ingredients,
            recipe_method=recipe_method,
            recipe_img=recipe_img,
            user_id=user_id,
            post_date=post_date
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("recipes", cuisine_id=cuisine_id))
    return render_template("add_recipe.html", cuisines=cuisines)


# === Edit Recipe Form ===
@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    cuisines = Cuisine.query.order_by(Cuisine.cuisine_type).all()

    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name")
        recipe.cuisine_id = request.form.get("cuisine_id")
        recipe.recipe_description = request.form.get("recipe_description")
        recipe.recipe_serves = request.form.get("recipe_serves")
        recipe.recipe_ingredients = request.form.get("recipe_ingredients")
        recipe.recipe_method = request.form.get("recipe_method")
        recipe.recipe_img = request.form.get("recipe_img")
        user_id = session.get("user_id")
        recipe.post_date = get_todays_date()

        db.session.commit()
        return redirect(url_for("recipes",
                                cuisine_id=recipe.cuisine_id))

    return render_template("edit_recipe.html",
                           recipe=recipe, cuisines=cuisines)


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    cuisine_id = recipe.cuisine_id
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("recipes", cuisine_id=cuisine_id))


# === Rate Recipe Form ===
@app.route("/rate_recipe/<int:id>", methods=["POST"])
def rate_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if request.method == "POST":
        rating = request.form.get("recipe_rating")
        if rating is not None:
            rating = int(rating)
            if recipe.rating is None:
                recipe.rating = [rating]
            else:
                recipe.rating.append(rating)
            flag_modified(recipe, "rating")
            db.session.commit()
            if recipe.rating:
                average_rating = sum(recipe.rating) / len(recipe.rating)
                recipe.average_rating = average_rating
            else:
                recipe.average_rating = None
            db.session.commit()
    return redirect(url_for("recipe", id=id))
