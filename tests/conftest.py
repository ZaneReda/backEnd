import pytest
from backend_api.models import Recipe
from backend_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe('test', 'test', 'test', False, 2)
    db.session.add(recipe)
    db.session.commit()
    with app.test_client() as testing_client:
        yield testing_client
    
    db.drop_all()


