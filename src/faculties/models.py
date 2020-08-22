from django.db import models

class Faculty(models.Model):
    faculty = models.CharField(max_length=500, null=False)


class Meta:
    verbose_name = 'Faculty'
    verbose_name_plural = 'Faculties'