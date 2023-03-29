# from ninja import Router
from ninja import NinjaAPI
from .auth_api import router as auth_router
from .profile import router as profile_router

api = NinjaAPI(title="POC API V1")

api.add_router("/", auth_router)
api.add_router("/profile/", profile_router)
