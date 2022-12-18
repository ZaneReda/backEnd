
from backend_api.models import Recipe
from backend_api import db, app
import pytest

def test_create_recipe(): 
    recipe = Recipe(name='test', ingredients='test', instructions='test', favorite=False, rating=0)
    db.session.add(recipe)
    db.session.commit()
    assert recipe.id == 1
    assert recipe.name == 'test'
    assert recipe.ingredients == 'test'
    assert recipe.instructions == 'test'
    assert recipe.favorite == False
    assert recipe.rating == 0


