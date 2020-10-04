from django.shortcuts import render
from .models import UserKeywords
from .serializers import UserKewordsSerializer
from rest_framework import viewsets

class UserKeywordsViewset(viewsets.ModelViewSet):
    queryset = UserKeywords.objects.all()
    serializer_class = UserKewordsSerializer
