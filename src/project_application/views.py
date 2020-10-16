from .models import ProjectApplication
from .serializers import ProjectApplicationSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny;

class ProjectApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectApplicationSerializer
    queryset = ProjectApplication.objects.all()
    permission_classes = [AllowAny]

    