from django.contrib import admin
from .models import Car, City, BrandCar, ModelCar, TransmissionCar


class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]


class CityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in City._meta.fields]


class BrandCarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BrandCar._meta.fields]


class ModelCarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ModelCar._meta.fields]


class TransmissionCarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TransmissionCar._meta.fields]


admin.site.register(Car, CarAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(BrandCar, BrandCarAdmin)
admin.site.register(ModelCar, ModelCarAdmin)
admin.site.register(TransmissionCar, TransmissionCarAdmin)
