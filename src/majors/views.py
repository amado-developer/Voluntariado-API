from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Major
from faculties.models import Faculty
from .serializers import MajorSerializer

class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

    @action(methods=['GET'], detail=False, url_path='majors-by-faculty')
    def mayors_by_faculty(self, request):
        search_filter = request.query_params['faculty']
        faculty = Faculty.objects.get(faculty__contains=search_filter)
        majors = Major.objects.filter(faculty=faculty)
        majors_response = MajorSerializer(majors, many = True).data
      
        return Response(majors_response)



