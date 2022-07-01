from django.db import models
from events_api.models import Event


# Create your models here.
class EmployeeItem(models.Model):
    name = models.CharField(max_length=100)
    item = models.CharField(max_length=50)
    party = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.item
