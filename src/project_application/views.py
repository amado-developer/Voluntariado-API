from .models import ProjectApplication
from project_request.models import ProjectRequest
from project_request.serializers import ProjectRequestSerializer
from .serializers import ProjectApplicationSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class ProjectApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectApplicationSerializer
    queryset = ProjectApplication.objects.all()
    permission_classes = [AllowAny]

    @action(methods=['GET'], detail=False, url_path='by-id')
    def by_id(self, request):
        project_id = request.query_params['id']
        projects = ProjectApplication.objects.filter(project_id=project_id)
        return Response(ProjectApplicationSerializer(projects, many=True).data)

