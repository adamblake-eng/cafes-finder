from rest_framework import serializers
from .models import Cafe, Barrio, Reviewer, Review

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ['name', 'join_date']

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['id', 'name', 'barrio', 'address', 'rating', 'has_good_medialunas', 'notes', 'recommendation_count']
    
    def get_barrio(self, obj):
        return obj.barrio.label
    
    def get_summary(self, obj):
        return f"{obj.name} is a {obj.rating}-star cafe."
    
class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = ['name', 'comuna']

class ReviewSerializer(serializers.ModelSerializer):
    cafe_name = serializers.ReadOnlyField(source="cafe.name")
    reviewer_name = serializers.ReadOnlyField(source="reviewer.name")
    class Meta:
        model = Review
        fields = ['id', 'cafe', 'cafe_name', 'reviewer', 'reviewer_name', 'comment', 'rating']