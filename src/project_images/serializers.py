from rest_framework import serializers
from .models import ProjectImages

class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = (
            'id',
            'image',
            'ifk',
        )
