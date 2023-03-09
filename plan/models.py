from django.db import models

from core.models import Crop

class FertilizerTemplate(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    stage = models.CharField(max_length=100)
    fertilizer = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    npk = models.CharField(max_length=100)
    application = models.CharField(max_length=100)

class PesticideTemplate(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    stage = models.CharField(max_length=100)
    pesticide = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    application = models.CharField(max_length=100)

class InsecticideTemplate(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    stage = models.CharField(max_length=100)
    insecticide = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    application = models.CharField(max_length=100)


# Create your models here.
