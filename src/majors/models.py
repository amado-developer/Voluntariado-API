from django.db import models

class Major(models.Model):
    major = models.CharField(max_length=500, null=False)
    faculty = models.ForeignKey(to='faculties.Faculty', on_delete=models.CASCADE)

class Meta:
    verbose_name = "Major"
    verbose_name_plural = "Majors"

