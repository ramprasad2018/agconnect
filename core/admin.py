from django.contrib import admin
from .models import Crop, Pesticide, Fertilizer, Insecticide

# Register your models here.


@admin.register(Fertilizer)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Insecticide)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Pesticide)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('type',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            queryset = queryset.filter(
                **{f'{self.search_fields[0]}__icontains': search_term})
        return queryset, use_distinct

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "type":
            return UniqueFarmNameChoiceField(queryset=self.model.objects.values('type').distinct().order_by('type'), label="Search by Type")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
