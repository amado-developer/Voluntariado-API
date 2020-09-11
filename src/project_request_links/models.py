from django.db import models


class ProjectRequestLinks(models.Model):
    link = models.URLField(null=False)
    project_request = models.ForeignKey(
        to='project_request.ProjectRequest', 
        null=False, 
        on_delete=models.CASCADE)

class Meta:
    verbose_name = 'Solicitud de Proyecto'
    verbose_name_plural = 'Solicitudes de Proyecto'
