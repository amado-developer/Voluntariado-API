from django.db import models

class ProjectApplication(models.Model):
    project_id  = models.ForeignKey(to='project_request.ProjectRequest', on_delete=models.CASCADE) 
    student_id  = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    major_id    = models.ForeignKey(to='majors.Major', on_delete=models.CASCADE)


class Meta:
    verbose_name = 'Project Application'
    verbose_name_plural = 'Projects Application'


