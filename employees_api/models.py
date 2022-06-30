from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(blank=True, null=True)
    item = models.CharField(max_length=100)

