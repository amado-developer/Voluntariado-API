from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ProjectRequestImages
from project_request.models import ProjectRequest
from .serializers import ProjectRequestImagesSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import permission_classes
class ProjectRequestImagesViewSet(viewsets.ModelViewSet):
    queryset = ProjectRequestImages.objects.all()
    serializer_class = ProjectRequestImagesSerializer


    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'save_images':
            permission_classes = [AllowAny]
        elif self.action == 'get_images':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(methods=['POST'], detail=False, url_path='save-images')
    def save_images(self, request):
        project_object = Solicitud_Proyecto.objects.last()
        images_querydict = request.data
        images_dict = dict(images_querydict)
        images_list = images_dict['image']
        
        for image in images_list:
            images = ProjectRequestImages()
            images.ifk = project_object
            images.image = image
            images.save()

        return Response({})


    @action(methods=['GET'], detail=False, url_path='get-images')
    def get_images(self, request):
        project_id = request.query_params['project']
        project = Solicitud_Proyecto.objects.get(pk=project_id)
        images = ProjectRequestImages.objects.filter(ifk=project)
        images_response = ProjectRequestImagesSerializer(images, many=True).data
        return Response(images_response)
