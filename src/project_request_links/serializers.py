from rest_framework import serializers
from .models import ProjectRequestLinks

class ProjectRequestLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRequestLinks
        fields = (
            'id',
            'link',
            'project_request',
        )