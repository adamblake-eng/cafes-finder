import pytest
from cafes.models import Barrio, Cafe
from rest_framework.test import APIClient



@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def make_barrio():
    # 1. Define an inner function that accepts **kwargs
    def inner(**kwargs):
        defaults = {
            "name" : "Default Barrio",
            "slug" : "default-barrio",
            "comuna" : 0
        }

        defaults.update(kwargs)

        return Barrio.objects.create(**defaults)

    return inner
        
@pytest.fixture
def make_cafe(make_barrio):
    
    def inner(**kwargs):

        if "barrio" not in kwargs:
            kwargs["barrio"] = make_barrio()

        defaults = {
            "name":"Default Cafe",
            "address":"Default Address"   
        }

        defaults.update(kwargs)

        return Cafe.objects.create(**defaults)

    return inner

