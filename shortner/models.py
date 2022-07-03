from django.db import models

# Create your models here.

class Link(models.Model):
    url = models.CharField(max_length=200)
    uid = models.CharField(max_length=50)