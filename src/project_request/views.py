from project_request.models import ProjectRequest
from project_request.serializers import ProjectRequestSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions

from rest_framework import viewsets
from majors.models import Major
from faculties.models import Faculty
from users.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.core.mail import send_mail

class ProjectRequestViewSet(viewsets.ModelViewSet):
    serializer_class= ProjectRequestSerializer
    queryset = ProjectRequest.objects.all()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='post-request')
    def post_request(self, request):
        project_request_querydict = request.data
        project_request_dict = dict(project_request_querydict)
        faculty_object = Faculty.objects.get(faculty=project_request_dict['faculty'])
        major_object = Major.objects.get(major=project_request_dict['major'], faculty=faculty_object)
        project_request = ProjectRequest()
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
        requests = ProjectRequest.objects.filter(is_approved=False)
        return Response(ProjectRequestSerializer(requests, many=True).data)

    @action(detail=False, methods=['get'], url_path='available-projects', permission_classes=[AllowAny])
    def available_projects(self, request):
        requests = ProjectRequest.objects.filter(is_approved=True)
        return Response(ProjectRequestSerializer(requests, many=True).data)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='send-request-email')
    def send_request_email(self, request):
        major = request.data['major']   
        project_request = ProjectRequest.objects.last()
        request_major = project_request.major
        principal = User.objects.get(major=request_major, is_staff=True)
        principal_firstname = principal.first_name
        principal_lastname = principal.last_name
        principal_email = principal.email
        company = request.data['company']
        project_name = request.data['projectName']
        subject = 'Solicitud de Nuevo Proyecto - Horas de Extensión'
        message = '''Estimado {} {}, la organización {} ha enviado una solicitud para el proyecto de horas de extensión "{}".
        '''.format(principal_firstname, principal_lastname, company, project_name)
        sender = 'horasdeextensionuvg@gmail.com'
        fail_silently=False
        result = send_mail(subject, message, sender, [principal_email], fail_silently)
        return Response(result)
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='send-notification-email')
    def send_notification_email(self, request):
        email = request.data['email']
        company = request.data['company']
        project = request.data['projectName']
        project_request = ProjectRequest.objects.last()
        subject = 'Universidad del Valle de Guatemala - Solicitud creada con éxito'
        message = ''' Estimados {}, su solicitud del proyecto "{}" ha sido enviada correctamente, nos estaremos comunicando con ustedes. '''.format(company, project)
        sender = 'horasdeextensionuvg@gmail.com'
        fail_silently=False
        result = send_mail(subject, message, sender, [email], fail_silently)
        return Response(result)
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='send-confirmation-email')
    def send_confirmation_email(self, request):
        email = request.data['email']
        company = request.data['company']
        project = request.data['project']
        isApproved = request.data['isApproved']
        subject = 'Universidad del Valle de Guatemala - Solicitud de proyecto'
        message = ''
        sender = 'horasdeextensionuvg@gmail.com'
        fail_silently=False
        print(type(isApproved))
        if isApproved == True:
            message = ''' Estimados {}, su solicitud del proyecto "{}" ha sido aprobada, puede ingresar con su usuario para llevar el seguimiento del proyecto.'''.format(company, project)
        else:
            message = ''' Estimados {}, su solicitud del proyecto "{}" no ha sido aprobada/ mueranse/ blokiados/ F'''.format(company, project)
        result = send_mail(subject, message, sender, [email], fail_silently)
        return Response({})

