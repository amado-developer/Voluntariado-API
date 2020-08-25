from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, UserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, profile_picture, age, 
    phone_number, password, password2, is_admin):
        if password != password2:
            raise ValueError('passwords does not match')
        else:
            user = self.model(
                email=self.normalize_email(email),
                first_name = first_name,
                last_name = last_name,
                profile_picture = profile_picture,
                age = age, 
                phone_number = phone_number,
            )
            user.is_admin = is_admin
            user.set_password(password)

            return user
            
class User(AbstractBaseUser):
    user_id         = models.CharField(max_length=20, null=True)
    email           = models.EmailField(unique=True)
    first_name      = models.CharField(max_length=50, null=False)
    last_name       = models.CharField(max_length=50, null=False)
    profile_picture = models.ImageField(max_length=None, null=True)
    age             = models.IntegerField(null=True)
    phone_number    = models.CharField(max_length=50, null=False)
    is_admin        = models.BooleanField(default=False)
    major         =  models.ForeignKey(to='majors.Major', on_delete=models.CASCADE, default=0)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    
class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'