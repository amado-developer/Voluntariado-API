from django.db import models

# nombre de la empresa varchar (200) not null
# nombre del proyecto varchar not null
# Descripcion varchar (500) not null
# Requerimientos varchar (500) not null
# Foto imagefield null

class Solicitud_Proyecto(models.Model):
    company_name = models.CharField(max_length=500, null=False)
    project_name = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=5000, null=False)
    requirements = models.CharField(max_length=5000, null=False)
    is_approved = models.BooleanField(default=False)
    picture = models.ImageField(null=True)
    phone_number = models.CharField(max_length=20, null=False, default='')
    email_address= models.EmailField(max_length=200,null=False, default='' )

class Meta():
    verbose_name = 'Solicitud de Proyecto'
    verbose_name_plural = 'Solicituedes de Proyecto'