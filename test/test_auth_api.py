import pytest
from django.test import Client
import json

from django.contrib.auth.models import User
from confest import *


@pytest.mark.django_db
def test_register():
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "password": "test123",
        "confirm_password": "test123",
    }

    client = Client()
    response = client.post(
        "/api/register", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 200

    response = client.post(
        "/api/register", data=json.dumps(payload), content_type="application/json"
    )
    response_data = json.loads(response.content)
    assert response.status_code == 422
    assert response_data["detail"] == "this username is already registered"

    payload["username"] = "johndoe1"
    payload["confirm_password"] = "65464"
    response = client.post(
        "/api/register", data=json.dumps(payload), content_type="application/json"
    )
    response_data = json.loads(response.content)
    assert response.status_code == 422
    assert response_data["detail"] == "password mismatch"


@pytest.mark.django_db
def test_login_token(db_fixture_user):
    client = db_fixture_user[0]
    payload = {"username": "test_user", "password": "12345678"}

    response = client.post(
        "/api/login_token", data=json.dumps(payload), content_type="application/json"
    )
    resp = json.loads(response.content)
    assert response.status_code == 200
    assert "token" in resp

    payload["password"] = "jhvhjjhhjbhb"
    response = client.post(
        "/api/login_token", data=json.dumps(payload), content_type="application/json"
    )
    resp = json.loads(response.content)
    assert response.status_code == 400


@pytest.mark.django_db
def test_logout(db_fixture_user):
    client = db_fixture_user[2]
    response = client.get("/api/logout", content_type="application/json")
    assert response.status_code == 200
