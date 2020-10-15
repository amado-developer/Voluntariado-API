from .models import ProjectApplication
from rest_framework import serializers

class ProjectApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectApplication
        fields = (
            'id',
            'project_id',
            'student_id',
            'major_id',
        )

        