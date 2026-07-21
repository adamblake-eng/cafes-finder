from rest_framework import serializers
from .models import Cafe, Barrio, Reviewer

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ['name', 'join_date']

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['id', 'name', 'barrio', 'address', 'rating', 'has_good_medialunas', 'notes']
    
    def get_barrio(self, obj):
        return obj.barrio.label
    
    def get_summary(self, obj):
        return f"{obj.name} is a {obj.rating}-star cafe."
    
class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = ['name', 'comuna']










