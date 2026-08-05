from rest_framework import serializers
from .models import Cafe, Barrio, Reviewer, Review, Tag, Dish
from django.db import transaction

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = ['id', 'name', 'comuna', 'slug']

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'is_vegan']
        read_only_fields = ['cafe']
    
class ReviewSerializer(serializers.ModelSerializer):
    cafe_name = serializers.ReadOnlyField(source="cafe.name")
    reviewer_name = serializers.ReadOnlyField(source="reviewer.name")
    class Meta:
        model = Review
        fields = ['id', 'cafe_name', 'reviewer', 'reviewer_name', 'comment', 'rating']
        read_only_fields = ['cafe']

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ['name', 'join_date']

class CafeSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, required=False)
    barrio = BarrioSerializer(read_only=True)
    dishes = DishSerializer(many=True, required=False)

    tagline = serializers.SerializerMethodField()

    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    barrio_name = serializers.SlugRelatedField(
        queryset = Barrio.objects.all(),
        slug_field='name',
        source='barrio',
        write_only=True)

    tag_names = serializers.ListField(child=serializers.CharField(max_length=50), write_only=True, required=False)

    @transaction.atomic
    def create(self, validated_data):

        tag_names = validated_data.pop("tag_names", [])
        reviews_data = validated_data.pop("reviews", [])
        dish_data = validated_data.pop('dishes', [])
        cafe = Cafe.objects.create(**validated_data)

        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            cafe.tags.add(tag)

        for review in reviews_data:
            Review.objects.create(cafe=cafe, **review)

        for dish in dish_data:
            Dish.objects.create(cafe=cafe, **dish)

        return cafe

    class Meta:
        model = Cafe
        fields = ['id', 'name', 'barrio', 'barrio_name', 'address', 'has_good_medialunas', 'notes', 
                  'recommendation_count', 'review_count', 'tagline', 'tags', 'reviews', 'tag_names', 'dishes']
    
    def get_tagline(self, obj):
        count = obj.review_count
        if count == 0:
            return "Be the first to visit!"
        elif count >= 5:
            return "Local favorite 🔥"
        else:
            return "Hidden gem"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']