from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..controllers import resources as controller
from ..main import app
import pytest
from ..models import resources as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_order(db_session):
    resource_data = {
        "item": "cola",
        "amount": 50
    }

    resource_object = model.Resource(**resource_data)
    created_order = controller.create(db_session, resource_object)

    assert created_order is not None
    assert created_order.item == "cola"
    assert created_order.amount == 50