from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Cafe, Barrio, Reviewer, Review
from .serializers import CafeSerializer, BarrioSerializer, ReviewerSerializer, ReviewSerializer

class CafeViewSet(viewsets.ModelViewSet):
        
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all().order_by("-rating")
    
    @action(detail=True, methods=['get'])
    def recommend(self, request, pk):
        cafe = self.get_object()
        cafe.recommendation_count += 1
        cafe.save()
        return Response(status=204)

class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barrio.objects.all().order_by('name')
    serializer_class = BarrioSerializer

class ReviewerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer











