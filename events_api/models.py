from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    when = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    where = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)
    

    
    def __str__(self):
        return self.title


