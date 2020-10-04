from .models import UserKeywords
from rest_framework import serializers

class UserKewordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKeywords
        fields = (
            'id',
            'keywords',
            'user',
        )