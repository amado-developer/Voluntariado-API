from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import ProjectRequestLinks
from project_request.models import ProjectRequest
from .serializers import ProjectRequestLinksSerializer

class ProjectRequestLinksViewSet(viewsets.ModelViewSet):
    queryset = ProjectRequestLinks.objects.all()
    serializer_class = ProjectRequestLinksSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'save_links':
            permission_classes = [AllowAny]
        elif self.action == 'get_links':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


    @action(methods=['POST'], detail=False, url_path='save-links')
    def save_links(self, request):
        project_object = ProjectRequest.objects.last()
        links_querydict = request.data
        links_dict = dict(links_querydict)
        links_list = links_dict['link']
       
        for link in links_list:
            links = ProjectRequestLinks()
            links.project_request = project_object
            links.link = link
            links.save()

        return Response({})

    @action(methods=['GET'], detail=False, url_path='get-links')
    def get_links(self, request):
        project_id = request.query_params['project']
        project = ProjectRequest.objects.get(pk=project_id)
        links = ProjectRequestLinks.objects.filter(project_request=project)
        links_response = ProjectRequestLinksSerializer(links, many=True).data
        return Response(links_response)