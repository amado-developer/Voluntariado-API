from django.db import models
import datetime
from django.utils import timezone 

class Solicitud_Proyecto(models.Model):
    date = models.DateTimeField(default=timezone.now)
    company_name = models.CharField(max_length=500, null=False)
    project_name = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=5000, null=False)
    requirements = models.CharField(max_length=5000, null=False)
    is_approved = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=False, default='')
    email_address= models.EmailField(max_length=200,null=False, default='')

class Meta:
    verbose_name = 'Solicitud de Proyecto'
    verbose_name_plural = 'Solicitudes de Proyecto'