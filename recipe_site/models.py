from sqlalchemy.dialects.postgresql import ARRAY
from recipe_site import db


class Cuisine(db.Model):
    # schema for the Cuisine model
    id = db.Column(db.Integer, primary_key=True)
    cuisine_type = db.Column(db.String(25), unique=True, nullable=False)
    cuisine_img = db.Column(db.Text, unique=True, nullable=False)
    recipes = db.relationship("Recipe",
                              backref="cuisine",
                              cascade="all, delete",
                              lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='cuisine')

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.cuisine_type


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), nullable=False)
    cuisine_id = db.Column(db.Integer,
                           db.ForeignKey(
                            "cuisine.id",
                            ondelete="CASCADE"),
                           nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    recipe_serves = db.Column(db.Integer, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    recipe_img = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.Date, nullable=False)
    rating = db.Column(ARRAY(db.Integer))
    average_rating = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='recipe')

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return (
            "{0}- Recipe: {1} | Cuisine: {2} | "
            "Description: {3} | Serves: {4} | "
            "Ingredients: {5} | Method: {6} | Recipe Img: {7} | Date: {8} | "
            "Avg Rating: {9} |".format(
                self.id,
                self.recipe_name,
                self.cuisine_id,
                self.recipe_description,
                self.recipe_serves,
                self.recipe_ingredients,
                self.recipe_method,
                self.recipe_img,
                self.post_date,
                self.average_rating
                )
            )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    mailing_list = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"{self.f_name} {self.l_name}"
