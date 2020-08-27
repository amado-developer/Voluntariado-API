from rest_framework import serializers
from solicitud_proyecto.models import Solicitud_Proyecto

class Solicitud_Proyecto_Serializer(serializers.ModelSerializer):
    class Meta():
        model= Solicitud_Proyecto
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
    