from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, UserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, profile_picture, age, 
    phone_number, password, password2, is_staff, major):
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
                major = major,
            )
            user.is_staff = is_staff
            # user.is_staff(is_admin)
            user.set_password(password)

            return user
            
class User(AbstractBaseUser):
    college_id      = models.CharField(max_length=20, null=True)
    email           = models.EmailField(unique=True)
    first_name      = models.CharField(max_length=50, null=False)
    last_name       = models.CharField(max_length=50, null=False)
    profile_picture = models.ImageField(max_length=None, null=True)
    age             = models.IntegerField(null=True)
    phone_number    = models.CharField(max_length=50, null=False)
    is_staff        = models.BooleanField(default=False)
    major           = models.ForeignKey(to='majors.Major', on_delete=models.CASCADE, default=0)
    cv              = models.FileField(max_length=None, null=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    
    def update_cv(self, *args, **kwargs):
        self.cv.delete()
        # super().delete(*args, **kwargs)
class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'