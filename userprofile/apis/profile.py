from typing import List,Optional
from ninja import Schema

# from .router import router_url
from .auth_backend import token_auth
from userprofile.models import Profile 
from django.shortcuts import get_object_or_404

from ninja import Router


router = Router()


class ProfileResponse(Schema):
    phone_number: Optional[int]
    address: Optional[str]
    latitude: Optional[float]
    longitute: Optional[float]


class ProfileIn(ProfileResponse):
    pass


@router.get("/", response={200: ProfileResponse}, auth=token_auth())
def get_profile(request):
    return get_object_or_404(Profile, user=request.user)



@router.post("/", response=ProfileResponse, auth=token_auth())
def update_profile(request, payload: ProfileIn):
    profile = get_object_or_404(Profile, user=request.user)
    profile.phone_number = payload.phone_number
    profile.address = payload.address
    profile.latitude = payload.latitude
    profile.longitute = payload.longitute
    profile.save()
    return profile
