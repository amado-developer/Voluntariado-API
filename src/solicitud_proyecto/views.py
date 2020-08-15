from solicitud_proyecto.models import Solicitud_Proyecto
from solicitud_proyecto.serializers import Solicitud_Proyecto_Serializer
from rest_framework import viewsets

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class= Solicitud_Proyecto_Serializer
    queryset = Solicitud_Proyecto.objects.all()



