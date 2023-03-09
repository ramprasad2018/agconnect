from django.db import models
from enum import Enum

# Create your models here.


class Crop(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Pesticide(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Insecticide(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Fertilizer(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name
