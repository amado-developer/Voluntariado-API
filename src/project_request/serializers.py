from rest_framework import serializers
from project_request.models import ProjectRequest

class ProjectRequestSerializer(serializers.ModelSerializer):
    class Meta():
        model= ProjectRequest
        fields = (
            'id',
            'date',
            'company_name',
            'project_name',
            'description',
            'requirements',
            'is_approved',
            'email_address',
            'phone_number',
            'company_address',
            'about_us',
            'major',
            'tags',
        )
    