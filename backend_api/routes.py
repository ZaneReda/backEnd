from flask import Flask, request
from backend_api import app, db
from backend_api.models import Recipe

@app.route('/', methods=['POST'])
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'], favorite=data['favorite'], rating=data['rating'])
    db.session.add(new_recipe)
    db.session.commit()
    return format_recipe(new_recipe), 201

@app.route('/', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)

@app.route('/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    data = request.get_json()
    recipe.name = data['name']
    recipe.ingredients = data['ingredients']
    recipe.instructions = data['instructions']
    recipe.favorite = data['favorite']
    recipe.rating = data['rating']
    db.session.commit()
    return format_recipe(recipe)

@app.route('/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)


def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'favorite': recipe.favorite,
        'rating': recipe.rating,
        'date_created': recipe.date_created
    }