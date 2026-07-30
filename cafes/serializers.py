from rest_framework import serializers
from .models import Cafe, Barrio, Reviewer, Review, Tag
from django.db import transaction

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
    tagline = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    tag_names = serializers.ListField(child=serializers.CharField(max_length=50), write_only=True)

    @transaction.atomic
    def create(self, validated_data):

        tag_names = validated_data.pop("tag_names", [])
        reviews_data = validated_data.pop("reviews", [])
        cafe = Cafe.objects.create(**validated_data)

        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            cafe.tags.add(tag)

        for review in reviews_data:
            Review.objects.create(cafe=cafe, **review)

        return cafe

    class Meta:
        model = Cafe
        fields = ['id', 'name', 'barrio', 'address', 'has_good_medialunas', 'notes', 
                  'recommendation_count', 'review_count', 'tagline', 'tags', 'reviews', 'tag_names']
    
    def get_tagline(self, obj):
        count = obj.review_count
        if count == 0:
            return "Be the first to visit!"
        elif count >= 5:
            return "Local favorite 🔥"
        else:
            return "Hidden gem"
    
class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = ['name', 'comuna']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']