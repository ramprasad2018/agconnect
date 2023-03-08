from django.db import models
from enum import Enum

# Create your models here.


class Crop(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name
