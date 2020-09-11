from rest_framework import serializers
from .models import ProjectRequestImages

class ProjectRequestImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRequestImages
        fields = (
            'id',
            'image',
            'ifk',
        )
