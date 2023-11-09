from flask import render_template, request, redirect, url_for, abort, g, session, flash
from functools import wraps
from sqlalchemy import func
from sqlalchemy.orm.attributes import flag_modified
from datetime import datetime
from recipe_site import app, db
from recipe_site.models import Cuisine, Recipe, User


@app.before_request
def load_user():
    user_id = session.get('user_id')
    g.user = User.query.get(user_id) if user_id is not None else None
    print(f"load_user - g.user: {g.user}")


def get_todays_date():
        today = datetime.today()
        return today


@app.route("/")
def home():
    recipes = Recipe.query.order_by(Recipe.id).all()
    for recipe in recipes:
        if recipe.average_rating is None:
            recipe.average_rating = 0
    return render_template("base.html", recipes=recipes)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        f_name = request.form.get("f_name")
        l_name = request.form.get("l_name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        mailing_list = request.form.get("mailing_list") == 'on'
        # checks if 'password' matches 'confirm_password'
        if password != confirm_password:
            # flash("Passwords must match", "error")
            return redirect(url_for("sign_up"))
        # checks if the username is already taken
        if User.query.filter_by(username=username).first():
            # flash("Username already taken, please choose another.", "error")
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
        # flash("Account created successfully! You can now log in.", "success")
        return redirect(url_for("sign_in"))
    return render_template("sign_up.html")  


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['user_id'] = user.id
            g.user = user
            print(f"sign_in - g.user: {g.user}")
            # flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            # flash("Invalid username or password", "error")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


@app.route("/sign_out")
def sign_out():
    session.pop('user_id', None)
    return redirect(url_for("home"))


@app.route("/cuisine")
def cuisine():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    return render_template("cuisine.html", cuisines=cuisines)


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = Cuisine(
            cuisine_type=request.form.get("cuisine_type"),
            cuisine_img=request.form.get("cuisine_img"),
            user_id = session.get('user_id')
        )
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
    cuisine_id = request.args.get('cuisine_id')
    if cuisine_id:
        recipes = Recipe.query.filter_by(cuisine_id=cuisine_id).order_by(Recipe.id).all()
        cuisine = Cuisine.query.get(cuisine_id)
        cuisine_type = cuisine.cuisine_type
    else:
        recipes = Recipe.query.order_by(Recipe.id).all()
        cuisine_type = "All Cuisines"

    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    return render_template("recipes.html", recipes=recipes, cuisines=cuisines, cuisine_type=cuisine_type)


@app.route("/recipe/<int:id>")
def recipe(id):
    recipe = Recipe.query.get(id)
    return render_template("recipe.html", recipe=recipe)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    if request.method == "POST":
        recipes = Recipe(
            recipe_name=request.form.get("recipe_name"),
            cuisine_id=request.form.get("cuisine_id"),
            recipe_description=request.form.get("recipe_description"),
            recipe_serves=request.form.get("recipe_serves"),
            recipe_ingredients=request.form.get("recipe_ingredients"),
            recipe_method=request.form.get("recipe_method"),
            recipe_img=request.form.get("recipe_img"),
            user_id = session.get('user_id'),
            post_date=get_todays_date()
        )
        db.session.add(recipes)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_recipe.html", cuisines=cuisines)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_type).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name"),
        recipe.cuisine_id = request.form.get("cuisine_id"),
        recipe.recipe_description = request.form.get("recipe_description"),
        recipe.recipe_serves = request.form.get("recipe_serves"),
        recipe.recipe_ingredients = request.form.get("recipe_ingredients"),
        recipe.recipe_method = request.form.get("recipe_method"),
        recipe.recipe_img=request.form.get("recipe_img"),
        user_id = session.get('user_id'),
        recipe.post_date=get_todays_date()
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))


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
            # updates the 'rating' column with the modified array so that each time the form is submitted, the array is modified accordingly.
            flag_modified(recipe, "rating")
            db.session.commit()
            if recipe.rating:
                # calculates the mean average of all values in the 'rating' array and updates the value in the'average_rating' column.
                average_rating = sum(recipe.rating) / len(recipe.rating)
                recipe.average_rating = average_rating
            else:
                recipe.average_rating = None
            db.session.commit()
    return redirect(url_for("recipe", id=id))
