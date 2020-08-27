from rest_framework import serializers
from users.models import User
import uuid

from rest_framework import permissions
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'inpute_type' : 'password'}, write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'profile_picture',
            'password',
            'password2',
            'age',
            'phone_number',
            'is_staff',
        )
  
        extra_kwargs = {
            'password' :{'write_only' : True },
        }

    def save(self):      
        user = User(
        email=self.data['email'],
        first_name = self.data['first_name'],
        last_name = self.data['last_name'],
        profile_picture= self.data['profile_picture'],
        age = self.data['age'],
        phone_number = self.data['phone_number'],
     )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Passwords must match'})
        user.is_admin = self.data['is_admin']
        user.set_password(password)
        user.save() 

        return user