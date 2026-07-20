from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cafe, Barrio, Comment, Reviewer
from .serializers import CafeSerializer, BarrioSerializer, CommentSerializer, ReviewerSerializer

class CafeViewSet(viewsets.ReadOnlyModelViewSet):
        # 1. queryset: Defines the collection of objects that this
        #    viewset will operate on. We'll get all cafes, ordered by rating
        # 2. serializer_class: Tells the viewset which serializer to use
        #    when converting the Cafe objects to JSON.
    serializer_class = CafeSerializer

    def get_queryset(self):
        # Start with your original collection of objects, ordered by rating
        queryset = Cafe.objects.all().order_by("-rating")

        # Check the URL for a ?barrio=... query parameter
        barrio_param = self.request.query_params.get("barrio")

        # If a barrio parameter was passed, filter down our ordered list
        if barrio_param is not None:
            queryset = queryset.filter(barrio__iexact=barrio_param)

        return queryset

class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barrio.objects.all().order_by('name')
    serializer_class = BarrioSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ReviewerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

def create_review(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









