import pytest
import json
from confest import *

from userprofile.models import Profile


@pytest.mark.django_db
def test_get_map_locations(db_fixture_user):
    client = db_fixture_user[2]
    request_user = db_fixture_user[1]
    Profile.objects.filter(user=request_user).update(
        address="Delhi, india", latitude=26.846695, longitute=80.946167
    )
    response = client.get("/api/map/", content_type="application/json")
    response_data = json.loads(response.content)
    profile_data = Profile.objects.exclude(
        latitude__isnull=True, longitute__isnull=True
    ).select_related("user")
    assert len(response_data) == profile_data.count() == 1
    assert response.status_code == 200
