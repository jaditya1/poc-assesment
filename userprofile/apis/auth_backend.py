import rest_framework.exceptions
from django.conf import settings
from ninja.security import HttpBearer
from rest_framework.authentication import TokenAuthentication


class NinjaAuthBearer(HttpBearer):
    """Adapter for django-ninja"""

    def authenticate(self, request, token: str):
        try:
            user, _ = TokenAuthBearer().authenticate(request)
            request.user = user
            return user
        except rest_framework.exceptions.AuthenticationFailed:
            return None


class TokenAuthBearer(TokenAuthentication):
    keyword = "Bearer"


def token_auth():
    return NinjaAuthBearer()
