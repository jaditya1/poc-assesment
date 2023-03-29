import pytest
from django.test import Client
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.fixture(scope="function")
def db_fixture_user():
    user = User.objects.create_user(username="test_user", password="12345678")
    client = Client()
    token, is_created = Token.objects.get_or_create(user=user)
    user_logged_in_client = APIClient()
    user_logged_in_client.credentials(HTTP_AUTHORIZATION="Bearer " + token.key)
    return client, user, user_logged_in_client
