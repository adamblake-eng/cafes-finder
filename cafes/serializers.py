from rest_framework import serializers
from .models import Cafe, Barrio, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['cafe', 'comment', 'reviewer_name']

    # We create a class that inherits from DRF's ModelSerializer.
class CafeSerializer(serializers.ModelSerializer):

    number_of_reviews = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True, source="review_set")
    summary = serializers.SerializerMethodField()
        # The Meta class is where we configure the serializer.
    class Meta:
            # 1. Tell the serializer which model it's based on.
        model = Cafe
            # 2. Define the "whitelist" of fields to include in the API.
        fields = ['id', 'name', 'barrio', 'address', 'rating', 'has_good_medialunas', 'summary', 'number_of_reviews', 'reviews']
    
    def get_barrio(self, obj):
        return obj.barrio.value
    
    def get_summary(self, obj):
        return f"{obj.name} is a {obj.rating}-star cafe."
    
    def get_number_of_reviews(self, obj):
        # 'obj' is the current Cafe instance.
        # .reviews comes from the 'related_name' we set on the ForeignKey!
        return obj.review_set.count()

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = ['name', 'comuna']










