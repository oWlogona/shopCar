from django.contrib import admin
from .models import Car, CityCar, BrandCar, ModelCar, TransmissionCar

admin.site.register(Car)
admin.site.register(CityCar)
admin.site.register(BrandCar)
admin.site.register(ModelCar)
admin.site.register(TransmissionCar)
