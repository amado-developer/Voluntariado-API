from django.db import models


class ProjectImages(models.Model):
    ifk = models.ForeignKey(to='solicitud_proyecto.Solicitud_Proyecto', on_delete=models.CASCADE)
    image = models.ImageField(default='')
    
