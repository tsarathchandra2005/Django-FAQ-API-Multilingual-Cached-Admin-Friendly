# from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework import generics
# from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer
# Create your views here.


class FAQListCreateView(generics.ListCreateAPIView):
    """ Handles listing and creating FAQ"""
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrivieng , updating , and deleting an FAQ"""
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
