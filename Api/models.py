from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.



class Tour(models.Model):
    name = models.CharField(max_length=55, blank=False)
    description = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return self.name

class Agent(models.Model):

    first_name = models.CharField(max_length=55, blank=False)
    last_name = models.CharField(max_length=55, blank=False)
    #group = models.OneToOneField(Group.objects.get(name='Agents'), on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


