from backend_api import app
import pytest

def test_get_recipe(testing_client):
    response = testing_client.get('/darecipes')
    assert response.status_code == 200


def test_dummy_wrong_route(): 

    with app.test_client() as client:
        response = client.get('/wrong_route')
        assert response.status_code == 404

def test_create_account(testing_client):
    response = testing_client.post('/darecipes', json={'name': 'test', 'ingredients': 'test', 'instructions': 'test', 'favorite': False, 'rating': 0})
    assert response.status_code == 201
