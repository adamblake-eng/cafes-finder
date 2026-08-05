import pytest
from cafes.models import Cafe

def test_client_fixture_exists(client):
    assert client is not None


@pytest.mark.django_db
def test_get_nonexistent_cafe_returns_404(client):
    
    response = client.get(path="/api/cafes/999/")
    
    assert response.status_code == 404


@pytest.mark.django_db
def test_create_cafe_via_api(client, make_barrio):

    barrio = make_barrio()

    payload = {
        "name" : "welqjbfiowuebfo",
        "address" : "ewmfwkneoifew",
        "barrio_name" : barrio.name
    }

    response = client.post(path="/api/cafes/", data=payload, format='json')

    assert response.status_code == 201
    assert response.data["name"] == "welqjbfiowuebfo"
    assert Cafe.objects.count() == 1


