from django.db import models
class Index(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
# Create your models here.
