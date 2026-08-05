import pytest
from cafes.models import Barrio, Cafe, Review, Reviewer, Tag
from django.db import IntegrityError
from django.core.exceptions import ValidationError


# LEVEL 1 TASK 1


@pytest.mark.django_db
def test_create_barrio():
    expected_name = "San Isidro"
    expected_slug = "san-isidro"
    expected_comuna = 67
    
    barrio = Barrio.objects.create(name=expected_name, slug=expected_slug, comuna=expected_comuna)
    
    assert barrio.name == expected_name
    assert barrio.slug == expected_slug
    assert barrio.comuna == expected_comuna
    assert barrio.id is not None


# LEVEL 1 TASK 2


@pytest.mark.django_db
def test_create_duplicate_barrio_errors():
    Barrio.objects.create(name = "Quilmes", slug = "quilmes", comuna = 69)
    
    with pytest.raises(IntegrityError):
        Barrio.objects.create(name = "Quilmes", slug = "quilmes", comuna = 69)


# CHECK BARRIO FIXTURE WORKS


@pytest.mark.django_db
def test_create_duplicate_barrio_errors(make_barrio):
    make_barrio()
    
    with pytest.raises(IntegrityError):
        make_barrio()


# CHECK CAFE FIXTURE WORKS


@pytest.mark.django_db
def test_create_cafe(make_cafe):
    
    cafe = make_cafe()
    
    assert cafe.name == "Default Cafe"
    assert cafe.address == "Default Address"
    assert cafe.barrio.name == "Default Barrio"


# LEVEL 1 TASK 3


@pytest.mark.django_db
def test_create_review_raises_validation_error():
    barrio = Barrio.objects.create(name = "Quilmes", slug = "quilmes", comuna = 69)
    cafe = Cafe.objects.create(
        barrio = barrio,
        name = "Quilmes cafe",
        address = "nwiodwhoidqwbo" 
        )
    reviewer = Reviewer.objects.create(name = "Sir Jon Smith")
    
    with pytest.raises(ValidationError):
        review = Review.objects.create(
            cafe=cafe, 
            reviewer=reviewer, 
            rating=6, 
            comment="neoiwdhoewihd"
            )
        review.full_clean()


# LEVEL 2 TASK 1


@pytest.mark.django_db
def test_cafe_defaults():
    barrio = Barrio.objects.create(name = "Quilmes", slug = "quilmes", comuna = 69)
    cafe = Cafe.objects.create(
        barrio = barrio,
        name = "Quilmes cafe",
        address = "nwiodwhoidqwbo" 
        )

    assert cafe.has_good_medialunas == False
    assert cafe.recommendation_count == 0


# LEVEL 2 TASK 2    


@pytest.mark.django_db
def test_cafe_string_representation():
    barrio = Barrio.objects.create(name = "Caballito", slug = "caballito", comuna = 360)
    cafe = Cafe.objects.create(
            barrio = barrio,
            name = "Musetta",
            address = "nwiodwhoidqwbo" 
            )

    result = str(cafe)

    assert result == "Musetta (Caballito (Comuna 360))"


# LEVEL 3 TASK 1


@pytest.mark.django_db
def test_cafe_tag_count_method_check():
    barrio = Barrio.objects.create(name = "Quilmes", slug = "quilmes", comuna = 69)
    cafe = Cafe.objects.create(
        barrio = barrio,
        name = "Quilmes cafe",
        address = "nwiodwhoidqwbo" 
        )
    tag = Tag.objects.create(name = "Good toilet seats")

    cafe.tags.add(tag)

    assert cafe.tags.count() == 1


# LEVEL 3 TASK 2


@pytest.mark.django_db
def test_cafe_review_count_check():
    barrio = Barrio.objects.create(name = "Quilmes", slug = "quilmes", comuna = 69)
    cafe = Cafe.objects.create(
        barrio = barrio,
        name = "Quilmes cafe",
        address = "nwiodwhoidqwbo" 
        )
    reviewer = Reviewer.objects.create(name = "Sir Jon Smith")
    review1 = Review.objects.create(
                cafe=cafe, 
                reviewer=reviewer, 
                rating=3, 
                comment="neoiwdhoewihd"
                )   
    review2 = Review.objects.create(
                cafe=cafe, 
                reviewer=reviewer, 
                rating=2, 
                comment="cnncsiaiugdwqig"
                ) 

    result = cafe.review_count

    assert result == 2

