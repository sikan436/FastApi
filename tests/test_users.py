from fastapi.testclient import TestClient
from app.main import app
from app import schemas
import pytest
from sqlalchemy.orm import Session

@pytest.fixture
def client():
    yield TestClient(app)

def test_root(client):
    response=client.get('/')
    print (response.json().get("message"))
    assert response.json().get("message")=="hello world dy "
    assert response.status_code==200


def test_createuser(client):
    response=client.post("/user",json={"email_id":"g14@gmail.com","password":"1234"})
    print (response.json())
    new_user=schemas.UserOut(**response.json())
    assert new_user.email_id=="g14@gmail.com"
    assert response.status_code==201