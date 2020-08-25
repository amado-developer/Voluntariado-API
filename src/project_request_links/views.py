from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ProjectRequestLinks
from solicitud_proyecto.models import Solicitud_Proyecto
from .serializers import ProjectRequestLinksSerializer

class ProjectRequestLinksViewSet(viewsets.ModelViewSet):
    queryset = ProjectRequestLinks.objects.all()
    serializer_class = ProjectRequestLinksSerializer


    @action(methods=['POST'], detail=False, url_path='save-links')
    def save_links(self, request):
        project_object = Solicitud_Proyecto.objects.last()
        links_querydict = request.data
        links_dict = dict(links_querydict)
        links_list = links_dict['link']
       
        for link in links_list:
            links = ProjectRequestLinks()
            links.project_request = project_object
            links.link = link
            links.save()

        return Response({})