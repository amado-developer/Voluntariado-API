from django.db import models
import datetime
from django.utils import timezone 

class ProjectRequest(models.Model):
    date = models.DateTimeField(default=timezone.now)
    company_name = models.CharField(max_length=500, null=False)
    project_name = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=5000, null=False)
    requirements = models.CharField(max_length=5000, null=False)
    is_approved = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=False, default='')
    email_address= models.EmailField(max_length=200,null=False, default='')
    company_address = models.CharField(max_length=1000, null=True)
    about_us = models.CharField(max_length=2000, null=True)
    major = models.ForeignKey(to='majors.Major', on_delete=models.CASCADE, default=0)
    tags = models.CharField(max_length=5000, null=True)

class Meta:
    verbose_name = 'Solicitud de Proyecto'
    verbose_name_plural = 'Solicitudes de Proyecto'