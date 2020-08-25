from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ProjectImages
from solicitud_proyecto.models import Solicitud_Proyecto
from .serializers import ProjectImagesSerializer

class ProjectImagesViewSet(viewsets.ModelViewSet):
    queryset = ProjectImages.objects.all()
    serializer_class = ProjectImagesSerializer


    @action(methods=['POST'], detail=False, url_path='save-images')
    def save_images(self, request):
        project_object = Solicitud_Proyecto.objects.last()
        images_querydict = request.data
        images_dict = dict(images_querydict)
        images_list = images_dict['image']
        
        for image in images_list:
            images = ProjectImages()
            images.ifk = project_object
            images.image = image
            images.save()

        return Response({})

    
    


