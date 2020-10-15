from .models import ProjectApplication
from .serializers import ProjectApplicationSerializer
from rest_framework import viewsets

class ProjectApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectApplicationSerializer
    queryset = ProjectApplication.objects.all()

    