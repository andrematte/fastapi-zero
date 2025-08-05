from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Hello World!'}
