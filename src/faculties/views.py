from rest_framework import viewsets
from .models import Faculty
from .serializers import FacultySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    




