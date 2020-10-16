from django.db import models

class ProjectApplication(models.Model):
    project_id  = models.IntegerField()
    student_id  = models.IntegerField()
    major_id    = models.IntegerField()

class Meta:
    verbose_name = 'Project Application'
    verbose_name_plural = 'Projects Application'


