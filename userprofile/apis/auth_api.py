from typing import List

from django.contrib.auth import authenticate, login, logout
from ninja import Schema
from pydantic import constr
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from ninja.errors import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from .auth_backend import token_auth

from ninja import Router


router = Router()


class LoginRequest(Schema):
    username: constr(to_lower=True)
    password: str


class RegisterRequest(Schema):
    first_name: str
    last_name: str
    username: constr(to_lower=True)
    password: str
    confirm_password: str


class RegisterResponse(Schema):
    message: str


class TokenLoginResponse(Schema):
    token: str


class LogoutResponse(Schema):
    message: str


@router.post("/register", response={200: RegisterResponse, 400: dict}, auth=None)
def register_user(request, payload: RegisterRequest):
    if User.objects.filter(username=payload.username).exists():
        raise ValidationError("this username is already registered")

    if payload.password != payload.confirm_password:
        raise ValidationError("password mismatch")
    User.objects.create_user(
        first_name=payload.first_name,
        last_name=payload.last_name,
        username=payload.username,
        password=payload.password,
    )

    return {"message": "User created successfully"}


@router.post("/login_token", response={200: TokenLoginResponse, 400: dict}, auth=None)
def login_token(request, payload: LoginRequest):
    """
    Required POST parameters: username, password
    For unsuccessful login, an HTTP 400 status code will be returned
    """

    serializer = AuthTokenSerializer(data=payload.dict())
    try:
        serializer.is_valid(raise_exception=True)
    except serializers.ValidationError as e:
        return 400, e.detail

    user: User = serializer.validated_data["user"]
    token, is_created = Token.objects.get_or_create(user=user)

    setattr(user, "token", token.key)
    return user


@router.get("/logout", response={200: LogoutResponse}, auth=token_auth())
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return LogoutResponse(message="Logged out")
