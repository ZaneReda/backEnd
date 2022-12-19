import pytest
from backend_api.models import Recipe


def test_create_recipe(): 
    recipe = Recipe('test', 'test', 'test', False, 0)
    assert recipe.name == 'test'
    assert recipe.ingredients == 'test'
    assert recipe.instructions == 'test'
    assert recipe.favorite == False
    assert recipe.rating == 0


