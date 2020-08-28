from solicitud_proyecto.models import Solicitud_Proyecto
from solicitud_proyecto.serializers import Solicitud_Proyecto_Serializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions

from rest_framework import viewsets
from majors.models import Major
from faculties.models import Faculty
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class= Solicitud_Proyecto_Serializer
    queryset = Solicitud_Proyecto.objects.all()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='post-request')
    def post_request(self, request):
        project_request_querydict = request.data
        project_request_dict = dict(project_request_querydict)
        faculty_object = Faculty.objects.get(faculty=project_request_dict['faculty'])
        major_object = Major.objects.get(major=project_request_dict['major'], faculty=faculty_object)
       
        project_request = Solicitud_Proyecto()
        project_request.company_name = project_request_dict['company_name']
        project_request.project_name = project_request_dict['project_name']
        project_request.description = project_request_dict['description']
        project_request.requirements = project_request_dict['requirements']
        project_request.phone_number = project_request_dict['phone_number']
        project_request.email_address = project_request_dict['email_address']
        project_request.company_address = project_request_dict['company_address']
        project_request.about_us = project_request_dict['about_us']
        project_request.major = major_object
        project_request.tags = project_request_dict['tags']
        project_request.save()
        return Response({})

    @action(detail=False, methods=['get'], url_path='pending-requests', permission_classes=[AllowAny])
    def pending_requests(self, request):
        requests = Solicitud_Proyecto.objects.filter(is_approved=False)
        return Response(Solicitud_Proyecto_Serializer(requests, many=True).data)


