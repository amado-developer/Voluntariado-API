from .models import ProjectApplication
from users.models import User
from users.serializers import UserSerializer
from rest_framework import serializers

class ProjectApplicationSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    class Meta:
        model = ProjectApplication
        fields = (
            'id',
            'project_id',
            'student_id',
            'student',
            'major_id',
        )
    
    def get_student(self, obj):
        student = User.objects.get(id=obj.student_id)
        return UserSerializer(student).data