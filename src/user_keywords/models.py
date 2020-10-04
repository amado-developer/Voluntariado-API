from django.db import models

class UserKeywords(models.Model):
    keywords = models.TextField(null=False)
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE)

class Meta:
    verbose_name = "User keyword"
    verbose_name_plural = "User keywords"
