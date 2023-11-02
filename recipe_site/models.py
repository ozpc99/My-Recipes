from recipe_site import db


class Cuisine(db.Model):
    # schema for the Cuisine model
    id = db.Column(db.Integer, primary_key=True)
    cuisine_type = db.Column(db.String(25), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="cuisine", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.cuisine_type



class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisine.id", ondelete="CASCADE"), nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    recipe_serves = db.Column(db.Integer, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    # recipe_img = 
    # author_name = db.Column(db.String(25), nullable=False)
    post_date = db.Column(db.Date, nullable=False)
    # is_featured = db.Column(db.Boolean, default=False, nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "{0}- Recipe: {1} | Cuisine: {2} | Description: {3} | Serves: {4} | Ingredients: {5} | Method: {6} | Date: {7}".format(
            self.id, self.recipe_name, self.cuisine_id, self.recipe_description, self.recipe_serves, self.recipe_ingredients, self.recipe_method, self.post_date
        )