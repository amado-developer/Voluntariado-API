from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from users.serializers import UserSerializer
from rest_framework import permissions
from .models import User

from rest_framework.decorators import action

def jwt_response_payload_handler(token, user=None, request=None):
    user = UserSerializer(user, context={'request': request}).data
    
    return {
        'token': token,
        'user': user,
    }

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['PATCH'], detail=False, url_path='update-student-cv')
    def update_student_cv(self, request):
        user_id = request.query_params['id']
        print(request.data)
        cv = request.data['file']
        user = User.objects.get(id = user_id)
        user.update_cv()
        user.cv = cv
        user.save()
        return Response("CV succesfully updated")