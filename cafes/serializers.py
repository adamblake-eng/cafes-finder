from rest_framework import serializers
from .models import Cafe, Barrio, Review


    # We create a class that inherits from DRF's ModelSerializer.
class CafeSerializer(serializers.ModelSerializer):

    summary = serializers.SerializerMethodField()
        # The Meta class is where we configure the serializer.
    class Meta:
            # 1. Tell the serializer which model it's based on.
        model = Cafe
            # 2. Define the "whitelist" of fields to include in the API.
        fields = ['id', 'name', 'barrio', 'address', 'rating', 'has_good_medialunas', 'summary']
    
    def get_summary(self, obj):
        return f"{obj.name} is a {obj.rating}-star cafe."

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = ['name', 'comuna']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['cafe', 'comment', 'reviewer_name']







