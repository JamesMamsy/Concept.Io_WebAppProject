from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Name', max_length=120)
    noProjects=0

