from django.contrib import admin
from .models import FertilizerTemplate, PesticideTemplate, InsecticideTemplate
# Register your models here.

@admin.register(FertilizerTemplate)
class CropAdmin(admin.ModelAdmin):
    list_display = ('stage', 'fertilizer')

@admin.register(PesticideTemplate)
class CropAdmin(admin.ModelAdmin):
    list_display = ('stage', 'pesticide')

@admin.register(InsecticideTemplate)
class CropAdmin(admin.ModelAdmin):
    list_display = ('stage', 'insecticide')
