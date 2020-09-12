from rest_framework import status, viewsets
from rest_framework.response import Response
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

    

