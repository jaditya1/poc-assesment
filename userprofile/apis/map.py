from .auth_backend import token_auth
from userprofile.models import Profile
from ninja import Router
from django.db.models import Q

router = Router()


@router.get("/", response={200: list}, auth=token_auth())
def get_map_locations(request):
    location_data = Profile.objects.select_related("user").values_list(
        "user__username", "address", "latitude", "longitute"
    )
    locations = [
        [f"{username} - {address}", latitude, longitude]
        for username, address, latitude, longitude in location_data
        if latitude and longitude and address
    ]
    return locations
