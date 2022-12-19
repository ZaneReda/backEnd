from backend_api import app
import pytest

def test_get_recipe(testing_client):
        response = testing_client.get('/1')
        assert response.status_code == 200
    

def test_dummy_wrong_route(): 
    with app.test_client() as client:
        response = client.get('/wrong_route')
        assert response.status_code == 404

def test_create_recipe(testing_client):
        response = testing_client.post('/', json={'name': 'test', 'ingredients': 'test', 'instructions': 'test', 'favorite': False, 'rating': 0})
        assert response.json['name'] == 'test'
        assert response.json['ingredients'] == 'test'
        assert response.json['instructions'] == 'test'
        assert response.json['favorite'] == False
        assert response.json['rating'] == 0
        assert response.status_code == 201

def test_update_recipe(testing_client):
        response = testing_client.put('/1', json={'name': 'test', 'ingredients': 'test', 'instructions': 'test', 'favorite': False, 'rating': 0})
        assert response.json['name'] == 'test'
        assert response.json['ingredients'] == 'test'
        assert response.json['instructions'] == 'test'
        assert response.json['favorite'] == False
        assert response.json['rating'] == 0
        assert response.status_code == 200

def test_delete_recipe(testing_client):
        response = testing_client.delete('/1')
        assert response.status_code == 200

def test_get_recipes(testing_client):
        response = testing_client.get('/')
        assert response.status_code == 200

