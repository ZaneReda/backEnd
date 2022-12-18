import pytest
from backend_api.models import Recipe
from backend_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe(name='test', ingredients='test', instructions='test', favorite=False, rating=0)
    db.session.add(recipe)
    db.session.commit()
    yield app.test_client()
    db.drop_all()

