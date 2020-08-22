from rest_framework import serializers
from .models import ProjectImages
class ProjectImagesSerializer():
    class Meta:
        model = ProjectImages
        fields = (
            'id',
            'image',
            'ifk',
        )
