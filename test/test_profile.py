import pytest
import json
from confest import *

from userprofile.models import Profile


@pytest.mark.django_db
def test_get_profile(db_fixture_user):
    client = db_fixture_user[2]
    request_user = db_fixture_user[1]
    response = client.get("/api/profile/", content_type="application/json")
    response_data = json.loads(response.content)
    profile_data = Profile.objects.filter(user=request_user).first()
    assert profile_data.phone_number == response_data["phone_number"]
    assert profile_data.address == response_data["address"]
    assert profile_data.latitude == response_data["latitude"]
    assert profile_data.longitute == response_data["longitute"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_profile(db_fixture_user):
    client = db_fixture_user[2]
    payload = {
        "phone_number": 9494949494,
        "address": "Lucknow, Up",
        "latitude": 21.12121,
        "longitute": 31.2565,
    }

    response = client.post(
        "/api/profile/", data=json.dumps(payload), content_type="application/json"
    )
    resp = json.loads(response.content)
    assert response.status_code == 200
    assert resp["phone_number"] == payload["phone_number"]
    assert resp["address"] == payload["address"]
    assert resp["latitude"] == payload["latitude"]
    assert resp["longitute"] == payload["longitute"]

    payload["address"] = None
    response = client.post(
        "/api/profile/", data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 422
