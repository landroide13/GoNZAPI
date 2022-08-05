from django.db import models

# Create your models here.

class Tour(models.Model):
    name = models.CharField(max_length=55, blank=False)
    description = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return self.name

class Agent(models.Model):
    first_name = models.CharField(max_length=55, blank=False)
    last_name = models.CharField(max_length=55, blank=False)
    department = models.CharField(max_length=55, default='Agent')

    def __str__(self):
        return self.first_name


