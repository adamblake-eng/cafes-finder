import pytest
from cafes.models import Barrio, Cafe, Review, Reviewer, Tag
from cafes.serializers import CafeSerializer, BarrioSerializer, ReviewSerializer

#TESTING GET REQUEST

@pytest.mark.django_db
def test_cafe_serializer_correctly_formats_tagline(make_cafe):

    cafe = make_cafe(name="Special Cafe")

    serializer = CafeSerializer(instance=cafe)

    data = serializer.data

    assert data["name"] == "Special Cafe"
    assert data["tagline"] == "Be the first to visit!"

   
#TESTING POST REQUEST

@pytest.mark.django_db
def test_review_serializer_rejects_invalid_rating(make_cafe):

    cafe = make_cafe()

    payload = {
        "cafe": cafe.id,
        "comment":"efjwoeifhoeiwf",
        "rating":10
    }

    serializer = ReviewSerializer(data=payload)

    assert serializer.is_valid() == False
    assert "rating" in serializer.errors




@pytest.mark.django_db
def test_tagline_is_hidden_gem_for_one_review(make_cafe):

    cafe = make_cafe()
    reviewer = Reviewer.objects.create(name="nmewkon")
    Review.objects.create(cafe=cafe, reviewer=reviewer, comment="nweofboew", rating=5)

    serializer = CafeSerializer(instance=cafe)

    data = serializer.data

    assert data["tagline"] == "Hidden gem"


@pytest.mark.django_db
def test_tagline_is_hidden_gem_for_six_review(make_cafe):

    cafe = make_cafe()
    reviewer = Reviewer.objects.create(name="nmewkon")

    for i in range(6):
        Review.objects.create(cafe=cafe, reviewer=reviewer, comment="nweofboew", rating=5)

    serializer = CafeSerializer(instance=cafe)

    data = serializer.data

    assert data["tagline"] == "Local favorite 🔥"




@pytest.mark.django_db
def test_cafe_serializer_reuses_existing_tags(make_barrio):

    barrio = make_barrio()
    tag = Tag.objects.create(name="Cozy")

    payload = {
        "barrio_name" : barrio.name,
        "name" : "jdioewnde",
        "address" : "ndowehdiew",
        "tag_names" : ["Cozy", "Cozy"]
    }

    serializer = CafeSerializer(data=payload)

    assert serializer.is_valid()
    cafe = serializer.save()

    assert cafe.tags.count() == 1
    assert Tag.objects.count() == 1
    assert serializer.instance.tags.first().name == "Cozy"






