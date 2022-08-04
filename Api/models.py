from django.db import models

# Create your models here.

class Tour(models.Model):
    name = models.CharField(max_length=55, blank=False)
    description = models.TextField(max_length=300, blank=False)


    




