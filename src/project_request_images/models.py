from django.db import models


class ProjectRequestImages(models.Model):
    ifk = models.ForeignKey(to='project_request.ProjectRequest', on_delete=models.CASCADE)
    image = models.ImageField(default='')
    
