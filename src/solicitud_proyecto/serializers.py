from rest_framework import serializers
from solicitud_proyecto.models import Solicitud_Proyecto

class Solicitud_Proyecto_Serializer(serializers.ModelSerializer):
    class Meta():
        model= Solicitud_Proyecto
        fields = (
            'id',
            'company_name',
            'project_name',
            'description',
            'requirements',
            'is_approved',
            'picture',
            'email_address',
            'phone_number'
        )
    