from django.shortcuts import render
from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Cafe, Barrio, Reviewer, Review
from .serializers import CafeSerializer, BarrioSerializer, ReviewerSerializer, ReviewSerializer

class CafeViewSet(viewsets.ModelViewSet):
        
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all().order_by("-rating")
    
    @action(detail=True, methods=['post'])
    def recommend(self, request, pk):
        cafe = self.get_object()
        cafe.recommendation_count = F('recommendation_count') + 1
        cafe.save()
        return Response(
        {
            "message": f"Successfully recommended {cafe.name}!",
            "recommendation_count": cafe.recommendation_count,
        },
        )
    
    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        cafes = Cafe.objects.filter(rating=5) 
        serializer = self.get_serializer(cafes, many=True) 
        return Response(serializer.data)


class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barrio.objects.all().order_by('name')
    serializer_class = BarrioSerializer

class ReviewerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer











